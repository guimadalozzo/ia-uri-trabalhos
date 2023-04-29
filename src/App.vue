<template>
    <div>
        <header>
            <h1>WordSpeech</h1>
        </header>
    </div>

    <div class="container">
        <div class="box" v-if="showStart">
            <p class="score title">Seja Bem-Vindo!</p>
            <button class="my-button" v-on:click="startTest">Iniciar Teste</button>
        </div>
        <div class="box" v-if="showComponent && counter < 5">
            <WordSpeech />
        </div>
        <div class="box" v-if="counter == 5">
            <p class="score">Parabéns! Você acertou {{ score }}/5!</p>
            <img src="https://media.tenor.com/vSB5J-sxmqUAAAAC/bravo-clapping.gif" style="width: 300px;">
        </div>
    </div>
</template>

<script>
import WordSpeech from './components/WordSpeech.vue';
export default {
    name: 'App',
    components: {
        WordSpeech
    },
    data() {
        return {
            showComponent: false,
            showStart: true,
            score: 0,
            counter: 0
        }
    },
    methods: {
        startTest() {
            this.showComponent = true
            this.showStart = false
        }
    }
}

</script>

<style>
body {
    background-color: #17a0e5;
    color: #fff;
    text-align: center;
    font-family: sans-serif;
    margin: 0px;

}

.container {
    width: 100%;
    height: 100%;
    background: #17a0e5;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
}

.box {
    width: 1200px;
    height: 450px;
    background-color: #fff;
    border-radius: 10px
}

h1 {
    margin-top: 30px;
    margin-bottom: 30px;
}

.score {
    font-size: 20px;
    color: black
}

.title {
    position: relative;
    top: 40%;
}

.my-button {
  background-color: #4CAF50; /* cor de fundo verde */
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  position: relative;
  top: 40%;
  border-radius: 5px; /* deixa as bordas do botão arredondadas */
  cursor: pointer; /* muda o cursor do mouse ao passar sobre o botão */
}

.my-button:hover {
  background-color: #3e8e41; /* escurece a cor de fundo quando o mouse passa sobre o botão */
}

</style>