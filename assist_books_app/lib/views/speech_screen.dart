import 'package:assist_books_app/models/book_model.dart';
import 'package:assist_books_app/provider/home_provider.dart';
import 'package:assist_books_app/views/book_detail_screen.dart';
import 'package:assist_books_app/widgets/book_widget.dart';
import 'package:avatar_glow/avatar_glow.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:speech_to_text/speech_to_text.dart';

import '../colors.dart';

class SpeechScreen extends StatefulWidget {
  const SpeechScreen({Key? key}) : super(key: key);

  @override
  State<SpeechScreen> createState() => _SpeechScreenState();
}

class _SpeechScreenState extends State<SpeechScreen> {
  SpeechToText speechToText = SpeechToText();
  final ScrollController _scrollController = ScrollController();
  HomeProvider? _provider;

  @override
  void initState() {
    super.initState();
    _provider = Provider.of<HomeProvider>(context, listen: false);
  }

  var pesquisado = false;
  var text = "Segure o botão e comece a falar";
  var isListening = false;
  var confidence = 1.0;

  @override
  Widget build(BuildContext context) {
    return Consumer<HomeProvider>(
      builder: (context, provider, widget) => Scaffold(
        appBar: _appBar(),
        floatingActionButtonLocation: FloatingActionButtonLocation.endFloat,
        floatingActionButton: AvatarGlow(
            animate: isListening,
            glowColor: bgColor,
            endRadius: 75.0,
            duration: const Duration(milliseconds: 2000),
            repeatPauseDuration: const Duration(milliseconds: 100),
            repeat: true,
            child: GestureDetector(
              onTapDown: (detail) async {
                setState(() => pesquisado = false);
                if (!isListening) {
                  var avaliable = await speechToText.initialize();
                  if (avaliable) {
                    setState(() => isListening = true);
                    speechToText.listen(
                      onResult: (val) => setState(() {
                        text = val.recognizedWords;
                        if (val.hasConfidenceRating && val.confidence > 0) {
                          confidence = val.confidence;
                        }
                      }),
                    );
                  }
                }
              },
              onTapUp: (detail) {
                setState(() => isListening = false);
                speechToText.stop();
                setState(() {
                  _provider?.books.clear();
                  var books = _provider?.getBooks(text);
                  books?.whenComplete(() => pesquisado = true);
                });
              },
              child: CircleAvatar(
                backgroundColor: bgColor,
                radius: 35,
                child: Icon(isListening ? Icons.mic : Icons.mic_none,
                    color: Colors.white),
              ),
            )),
        body: !pesquisado
            ? _column(provider)
            : provider.books.length <= 0
                ? const Center(
                    child: Text(
                      "Livro não encontrado",
                      style: TextStyle(
                          fontSize: 20,
                          color: Colors.black,
                          decoration: TextDecoration.none),
                    ),
                  )
                : _column(provider),
      ),
    );
  }

  AppBar _appBar() {
    return AppBar(
      title: Text('Confidence: ${(confidence * 100.0).toStringAsFixed(1)}%'),
      backgroundColor: bgColor,
    );
  }

  Widget _column(HomeProvider provider) {
    return Column(
      children: [
        Container(
          alignment: Alignment.center,
          padding: EdgeInsets.symmetric(horizontal: 24, vertical: 16),
          child: Text(
            text,
            style: TextStyle(
                fontSize: 20,
                color: Colors.black54,
                fontWeight: FontWeight.w600),
          ),
        ),
        Expanded(
            child: Stack(
          children: [
            Container(
              child: ListView.builder(
                primary: false,
                shrinkWrap: true,
                controller: _scrollController,
                scrollDirection: Axis.vertical,
                itemCount: provider.books.length,
                itemBuilder: (context, position) {
                  final book = provider.books[position];
                  return InkWell(
                    onTap: () {
                      _openBookDetail(book);
                    },
                    child:
                        BookWidget(book.title, book.subtitle, book.thumbnail),
                  );
                },
              ),
            ),
            provider.isLoading
                ? Center(child: CircularProgressIndicator())
                : SizedBox(),
          ],
        ))
      ],
    );
  }

  void _openBookDetail(BookModel book) {
    Navigator.push(
        context,
        MaterialPageRoute(
            builder: (context) => BookDetailScreen(book.title, book.subtitle, book.description, book.thumbnail, book.bookUrl)));
  }
}
