import 'package:flutter/material.dart';
import 'package:flutter_widget_from_html/flutter_widget_from_html.dart';
import 'package:url_launcher_platform_interface/url_launcher_platform_interface.dart';

import '../colors.dart';

class BookDetailScreen extends StatefulWidget {
  String? title;
  String? subtitle;
  String? description;
  String? thumbnail;
  String? bookUrl;
  BookDetailScreen(this.title, this.subtitle, this.description, this.thumbnail,
      this.bookUrl, {Key? key}) : super(key: key);

  @override
  State<BookDetailScreen> createState() => _BookDetailScreenState();
}

class _BookDetailScreenState extends State<BookDetailScreen> {
  final UrlLauncherPlatform launcher = UrlLauncherPlatform.instance;
  Future<void>? _launched;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Center(child: Text(widget.title!)),
        backgroundColor: bgColor,
      ),
      bottomNavigationBar: _bottomNavWidget(widget.bookUrl),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Padding(
              padding: EdgeInsets.only(left: 16, right: 16, top: 16),
              child: Text(
                "${widget.title}",
                style: TextStyle(
                    color: Colors.black,
                    fontWeight: FontWeight.bold,
                    fontSize: 18),
              ),
            ),
            Padding(
              padding: EdgeInsets.only(left: 16, right: 16, top: 16),
              child: Text(
                "${widget.subtitle ?? "-"}",
                style: TextStyle(color: Colors.black, fontSize: 14),
              ),
            ),
            Padding(
                padding: EdgeInsets.only(left: 16, right: 16, top: 16),
                child: Image.network(widget.thumbnail ?? "")),
            Padding(
                padding: EdgeInsets.only(left: 16, right: 16, top: 16),
                child: HtmlWidget(widget.description ?? "-")),
          ],
        ),
      ),
    );
  }

  Widget _bottomNavWidget(String? bookUrl) {
    final widget = Container(
      color: bgColor,
      child: const Padding(
        padding: EdgeInsets.all(16),
        child: Text(
          "Visitar página",
          textAlign: TextAlign.center,
          style: TextStyle(color: Colors.white, fontSize: 20),
        ),
      ),
    );
    return InkWell(
      child: widget,
      onTap: () async {
        if (bookUrl != null) {
          setState(() {
            _launched = _launchInBrowser(bookUrl);
          });
        }
      },
    );
  }

  Future<void> _launchInBrowser(String url) async {
    if (!await launcher.launch(
      url,
      useSafariVC: false,
      useWebView: false,
      enableJavaScript: false,
      enableDomStorage: false,
      universalLinksOnly: false,
      headers: <String, String>{},
    )) {
      throw Exception('Could not launch $url');
    }
  }
}