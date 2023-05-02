import 'dart:convert';

import 'package:flutter/widgets.dart';
import 'package:http/http.dart' as http;

import '../models/book_model.dart';

class HomeProvider with ChangeNotifier {
  List<BookModel> books = [];
  int page = 0;
  bool isLoading = false;

  Future<void> getBooks(String text) async {
    isLoading = true;
    try {
      final response = await http.get(Uri.parse(
          "https://www.googleapis.com/books/v1/volumes?q=$text"));

      //print("response.body ${response.body}");
      final items = jsonDecode(response.body)['items'];
      List<BookModel> bookList = [];
      for (var item in items) {
        bookList.add(BookModel.fromApi(item));
      }

      books.addAll(bookList);
      page += 40;
      isLoading = false;
      notifyListeners();
    } catch (e) {
      print("error get books $e");
      notifyListeners();
    }
  }

  void showLoading() {
    isLoading = true;
    notifyListeners();
  }
}
