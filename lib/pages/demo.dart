import 'dart:async';
import 'dart:io';

import 'package:dart_openai/openai.dart';
import 'package:flutter/material.dart';
import 'package:flutter_ffmpeg/flutter_ffmpeg.dart';
import 'package:flutter_sound_platform_interface/flutter_sound_recorder_platform_interface.dart';
import 'package:google_speech/generated/google/cloud/speech/v1/cloud_speech.pb.dart'
    as rR;
import 'package:google_speech/google_speech.dart';
import 'package:path_provider/path_provider.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:record_mp3/record_mp3.dart';
import 'package:text_to_speech/text_to_speech.dart';

const AudioSource theSource = AudioSource.microphone;

class Demo extends StatefulWidget {
  const Demo({
    super.key,
  });

  @override
  _DemoState createState() => _DemoState();
}

class _DemoState extends State<Demo> {
  String transcriptedText = '';
  String generatedText = '';
  bool lock = false;

  @override
  void initState() {
    super.initState();
    _checkStoragePermission();
  }

  Future<void> _createEmptyFiles() async {
    try {
      await File('${await _localPath}/audio.mp3').create(recursive: true);
      await File('${await _localPath}/audio.flac').create(recursive: true);
    } catch (e) {
      debugPrint(
        'LOG ? e.toString()',
      );
    }
    return;
  }

  Future<void> _checkStoragePermission() async {
    setState(() {
      lock = true;
    });
    await Permission.storage.request().then(
      (value) async {
        if (value.isGranted) {
          debugPrint('LOG ? Permission granted');
        } else {
          await Permission.storage.request();
        }
      },
    );
    await Permission.microphone.request().then(
      (value) async {
        if (value.isGranted) {
          debugPrint('LOG ? Permission granted');
        } else {
          await Permission.microphone.request();
        }
      },
    );
    await _createEmptyFiles();
    setState(() {
      lock = false;
    });
  }

  @override
  void dispose() {
    super.dispose();
  }

  void updateTranscriptedText(String text) {
    setState(() {
      transcriptedText = text;
    });

    if (transcriptedText != text) {
      updateTranscriptedText(text);
    }
  }

  Future<String> get _localPath async {
    final directory = await getTemporaryDirectory();
    return directory.path;
  }

  Future<String> get _localFile async {
    final path = await _localPath;
    return '$path/audio.mp3';
  }

  Future<List<int>> _getAudioContent() async {
    final PermissionStatus permissionStatus = await Permission.storage.status;

    if (!permissionStatus.isGranted) {
      await Permission.storage.request();
    }

    final FlutterFFmpeg _flutterFFmpeg = FlutterFFmpeg();

    String inputPath = await _localFile;

    String outputPath = '${await _localPath}/audio.flac';

    await _flutterFFmpeg.execute('-i $inputPath -vn -acodec flac $outputPath');

    return File(outputPath).readAsBytesSync().toList();
  }

  TextToSpeech tts = TextToSpeech();

  @override
  Widget build(BuildContext context) {
    return AbsorbPointer(
      absorbing: lock,
      child: Opacity(
        opacity: lock ? 0.5 : 1,
        child: Scaffold(
          appBar: AppBar(
            title: const Text(
              'Prova de Conceito',
            ),
            automaticallyImplyLeading: false,
            centerTitle: true,
          ),
          body: SingleChildScrollView(
            child: Padding(
              padding: const EdgeInsets.symmetric(
                horizontal: 20,
                vertical: 20,
              ),
              child: Column(
                children: <Widget>[
                  const Text(
                    'Todos os dados gerados serão apagados após requisitar um novo processamento.',
                  ),
                  SizedBox(
                    height: 80,
                    width: double.infinity,
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        ElevatedButton(
                          onPressed: () async {
                            String path = await _localPath;
                            String recordFilePath = '$path/audio.mp3';

                            RecordMp3.instance.status == RecordStatus.RECORDING
                                ? {
                                    RecordMp3.instance.stop(),
                                    WidgetsFlutterBinding.ensureInitialized()
                                        .addPostFrameCallback((timeStamp) {
                                      setState(() {});
                                    }),
                                  }
                                : {
                                    await _deleteFiles(),
                                    RecordMp3.instance
                                        .start(recordFilePath, (p0) => null),
                                    WidgetsFlutterBinding.ensureInitialized()
                                        .addPostFrameCallback((timeStamp) {
                                      setState(() {});
                                    }),
                                  };
                          },
                          child: Text(
                            RecordMp3.instance.status == RecordStatus.RECORDING
                                ? 'Parar'
                                : 'Gravar',
                          ),
                        ),
                        const SizedBox(
                          width: 20,
                        ),
                        Text(
                          RecordMp3.instance.status == RecordStatus.RECORDING
                              ? 'Gravando...'
                              : 'Gravação parada',
                        ),
                      ],
                    ),
                  ),
                  SizedBox(
                    height: 50,
                    child: FutureBuilder<String>(
                      future: _localFile,
                      builder: (BuildContext context,
                          AsyncSnapshot<String> snapshot) {
                        if (snapshot.hasData) {
                          return Text('Audio file path: ${snapshot.data}');
                        }

                        return Container();
                      },
                    ),
                  ),
                  ElevatedButton(
                    onPressed: () async {
                      const String mapKey = String.fromEnvironment(
                        'GOOGLE_API_KEY',
                      );

                      final ServiceAccount serviceAccount =
                          ServiceAccount.fromString(
                        mapKey,
                      );

                      final SpeechToText speechToText =
                          SpeechToText.viaServiceAccount(
                        serviceAccount,
                      );

                      final RecognitionConfig config = RecognitionConfig(
                        model: RecognitionModel.basic,
                        enableAutomaticPunctuation: true,
                        languageCode: 'pt-BR',
                        encoding: AudioEncoding.FLAC,
                        sampleRateHertz: 44100,
                      );

                      final List<int> audio = await _getAudioContent();

                      final rR.RecognizeResponse response =
                          await speechToText.recognize(config, audio);

                      updateTranscriptedText(
                        response.results.isNotEmpty
                            ? response
                                .results.first.alternatives.first.transcript
                            : 'Não foi possível transcrever o áudio',
                      );
                    },
                    child: const Text(
                      'Converter para texto',
                    ),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  Text(
                    'Texto transcrito: $transcriptedText',
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  ElevatedButton(
                    onPressed: () async {
                      OpenAICompletionModel completion =
                          await OpenAI.instance.completion.create(
                        model: 'text-davinci-002',
                        prompt: transcriptedText.characters.last == '?'
                            ? transcriptedText.replaceRange(
                                transcriptedText.length - 1,
                                transcriptedText.length,
                                '',
                              )
                            : transcriptedText,
                        maxTokens: 1000,
                        temperature: 0.5,
                        stop: '\n',
                        n: 1,
                        echo: true,
                      );

                      setState(() {
                        generatedText = completion.choices.first.text;
                      });
                    },
                    child: const Text(
                      'Obter versão do texto com aprimoramento',
                    ),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  Text(
                    'Texto gerado: $generatedText',
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  ElevatedButton(
                    onPressed: () async {
                      if (generatedText.isEmpty) {
                        return;
                      }
                      tts.speak(generatedText);
                    },
                    child: const Text(
                      'Reproduzir áudio',
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  Future<void> _deleteFiles() async {
    try {
      String path = await _localPath;

      final file = File('$path/audio.mp3');
      await file.delete();

      final file2 = File('$path/audio.flac');
      await file2.delete();
    } catch (e) {
      debugPrint(
        'LOG ? ${e.toString()}',
      );
    }
    return;
  }
}
