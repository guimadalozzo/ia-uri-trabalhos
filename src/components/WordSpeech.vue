<template>
    <div class="write">
        <p class="score">Sua Pontuação: {{ $parent.score }}</p>
        <p class="question">Qual palavra completa melhor a frase?</p>
        <div class="error-message" v-if="show_error">
            <p>{{ error_message }}</p>
        </div>
        <p class="phrase">{{ sentence.phrase }}</p>

        <p class="question">Pronuncie a palavra correta:
        <div class="microphone-box">
            <button type="button" v-bind:class="{ 'recording': isRecording }" class="microphone-button"
                v-on:click="toggleRecording">
                <img src="../assets/Img/mic.png" style="width: 30px; margin-top: -10px;">
            </button>
        </div>
        </p>
        <button class="item" v-for="item in items"
            v-bind:class="{ 'bg-green': is_correct && item === sentence.correct_word, 'bg-red': is_incorrect && item === current_text }">{{
                item }}</button>

        <div class="success-message" v-if="is_correct">
            <div class="message-text">Correto!</div>
            <div class="progress-bar"></div>
        </div>

        <div class="wrong-message" v-if="is_incorrect">
            <div class="message-text">Incorreto!</div>
            <div class="wrong-progress-bar"></div>
        </div>
    </div>
</template>

<script>
import $ from 'jquery'
import RecordRTC from 'recordrtc'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

export default {
    name: 'WordSpeech',
    data() {
        return {
            items: ['...', '...', '...', '...'],
            sentence: { 'phrase': "..." },
            show_error: false,
            error_message: "Error",
            is_correct: false,
            is_incorrect: false,
            current_text: "",
            isRecording: false,
            score: 0
        }
    },
    mounted() {
        $.ajax({
            url: 'http://127.0.0.1:5000/api/question',
            method: 'GET',
            dataType: 'json',
            success: (data) => {
                // Armazena a sentença (pergunta e resposta certa na variavel sentence)
                this.sentence = data[0]
                // Armazena as alternativas nos itens
                this.items = data[1]

                // Faz o tratamento na frase da sentença para apresentar ____ em fez de $
                this.sentence.phrase = this.sentence.phrase.replace(/\$/g, '___')
            },
            error: (error) => {
                console.log(error)
            },
        })
    },
    methods: {
        toggleRecording() {
            if (this.isRecording) {
                // parar a gravação
                this.recorder.stopRecording(() => {
                    this.audioBlob = this.recorder.getBlob()
                    this.recorder.destroy()
                    this.recorder = null
                    this.isRecording = false
                    this.saveRecording()
                })
            } else {
                // iniciar a gravação
                navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
                    this.recorder = RecordRTC(stream, {
                        type: 'audio',
                        mimeType: 'audio/webm',
                        recorderType: RecordRTC.StereoAudioRecorder,
                        desiredSampRate: 16000,
                    })
                    this.recorder.startRecording()
                    this.isRecording = true

                    this.show_error = false
                    this.error_message = "Error"

                    this.stopRecordingAfterDelay(3000)
                })
            }
        },
        stopRecordingAfterDelay(delayMs) {
            setTimeout(() => {
                if (this.isRecording) {
                    this.recorder.stopRecording(() => {
                        this.audioBlob = this.recorder.getBlob()
                        this.recorder.destroy()
                        this.recorder = null
                        this.isRecording = false
                        this.saveRecording()
                    })
                }
            }, delayMs)
        },
        saveRecording() {
            // envia a gravação para o servidor ou salva localmente
            const formData = new FormData()
            formData.append('audio', this.audioBlob, 'recording.webm')
            // faça uma requisição AJAX para enviar o arquivo para o servidor

            $.ajax({
                url: 'http://127.0.0.1:5000/api/recognition',
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
                success: (data) => {
                    console.log('Arquivo enviado com sucesso!')
                    console.log(data)

                    if (typeof (data) == 'object' && Object.keys(data).length != 0) {
                        let word = ""
                        let status = false

                        // Olha cada uma das opções e diz se é valido ou nao
                        data['alternative'].forEach((alternative) => {
                            console.log(alternative.transcript)
                            let value = this.judgeQuestion(alternative.transcript);
                            console.log(value)

                            // Se o valor vir nulo, a palavra era invalida
                            // Se o status vier false, significa que a palavra está mas é errada
                            // Se o status vier true, significa que a palavra está e é certa
                            // No último, caso, o if vai parar de executar, pois status = true
                            if (value != null && status == false) {
                                status = value[0]
                                word = value[1]
                            }
                        })

                        // Se word for diferente de "", significa que ele encontrou uma palavra da lista  
                        if (word != "") {
                            if (status) {
                                this.is_correct = true
                                this.is_incorrect = false

                                setTimeout(() => {
                                    this.$root.counter++
                                    this.$root.showComponent = false
                                    this.$nextTick(() => {
                                        this.$root.showComponent = true
                                    })
                                }, 3000)

                                this.$root.score++
                            } else {
                                this.is_correct = false
                                this.is_incorrect = true
                                this.current_text = word.toLowerCase()
                                
                                setTimeout(() => {
                                    this.$root.counter++
                                    this.$root.showComponent = false
                                    this.$nextTick(() => {
                                        this.$root.showComponent = true
                                    })
                                }, 3000)

                            }
                        } else {
                            this.show_error = true
                            this.error_message = "Erro: Palavra não identificada. Tente novamente!"
                        }
                    } else { // Significa que nao entendeu nenhuma palavra
                        this.show_error = true
                        this.error_message = "Erro: Palavra não identificada. Tente novamente!"
                    }
                },
                error: (error) => {
                    console.error('Erro ao enviar arquivo:', error)
                },
            })
        },
        judgeQuestion(alternative) {
            if (this.items.includes(alternative.toLowerCase())) { // Significa que a palavra está incluída entre as 4 opções
                if (alternative.toLowerCase() == this.sentence.correct_word.toLowerCase()) { // Verifica se valou a palavra certa
                    return [true, alternative]
                } else {
                    return [false, alternative]
                }
            } else {
                return null
            }
        }
    },
}
</script>



<style>
.write {
    padding-top: 20px;
    color: rgb(96, 100, 100);
    font-size: 40px;
}

.question {
    font-size: 30px;
}

.score {
    font-size: 20px;
}

.phrase {
    font-size: 25px;
    border-radius: 10px;
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);
    margin: 10px 20px;
    font-weight: bold;
}

.item {
    flex-direction: row;
    display: inline-block;
    margin-right: 20px;
    font-size: 30px;
    color: rgb(8, 68, 151);
    border-radius: 10px;
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);
    background-color: #fff;
    width: 250px;
}

.microphone-button {
    border-radius: 999px;
}

button {
    cursor: pointer;
}

.error-message {
    background-color: #ffcccc;
    border: 2px solid #ff0000;
    color: #ff0000;
    padding: 10px;
    border-radius: 5px;
    font-size: 20px;
    margin-bottom: 20px;
    height: 50px;
}

.bg-green {
    background-color: green;
    color: white;
}

.bg-red {
    background-color: red;
    color: white;
}

.microphone-button {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #f44336;
    color: #fff;
    border: none;
    outline: none;
    cursor: pointer;
    font-size: 30px;
    justify-content: center;
    align-items: center;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3);
}

.recording {
    background-color: rgb(85, 223, 85) !important;
}

.microphone-button:hover {
    background-color: #e53935;
}

.microphone-box {
    width: 100%;
    margin: auto;
}

.success-message {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100px;
    width: 100%;
    background-color: #a1f0c2;
    color: #000000;
    border-radius: 10px;
    position: relative;
    margin-top: 55px;
}

.message-text {
    font-size: 24px;
    font-weight: bold;
}

.progress-bar {
    position: absolute;
    bottom: 0;
    height: 5px;
    width: 100%;
    background-color: #07ce00;
    animation: progress-bar 3s linear;
}

.wrong-message {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100px;
    width: 100%;
    background-color: #f0a1a1;
    color: #000000;
    border-radius: 10px;
    position: relative;
    margin-top: 55px;
}

.wrong-progress-bar {
    position: absolute;
    bottom: 0;
    height: 5px;
    width: 100%;
    background-color: #ce0000;
    animation: progress-bar 3s linear;
}

@keyframes progress-bar {
    0% {
        width: 0;
    }

    100% {
        width: 100%;
    }
}

@keyframes wrong-progress-bar {
    0% {
        width: 0;
    }

    100% {
        width: 100%;
    }
}
</style>