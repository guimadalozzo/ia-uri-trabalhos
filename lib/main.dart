import 'package:dart_openai/openai.dart';
import 'package:flutter/material.dart';
import 'package:project/constants/routes.dart';
import 'package:project/route_generator.dart';

void main() {
  const String openAiApiKey = String.fromEnvironment(
    'OPEN_AI_API_KEY',
  );
  OpenAI.apiKey = openAiApiKey;

  runApp(
    const MyApp(),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Prova de Conceito',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: demo,
      onGenerateRoute: RouteGenerator.generateRoute,
    );
  }
}
