import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home: Scaffold(
      appBar: AppBar(
        title: Text('BMI Calculator'),
        backgroundColor: Colors.green,
      ),
      body: BMICalculator(),
    ),
  ));
}

Widget BMICalculator() {
  final weightController = TextEditingController();
  final heightController = TextEditingController();

  return StatefulBuilder(
    builder: (context, setState) {
      String result = "";

      void calculateBMI() {
        final weight = double.tryParse(weightController.text);
        final height = double.tryParse(heightController.text);

        if (weight == null || height == null || weight <= 0 || height <= 0) {
          setState(() {
            result = "Please enter valid weight and height values.";
          });
          return;
        }

        final bmi = weight / (height * height);
        String category = bmi < 18.5
            ? "Underweight"
            : bmi < 24.9
                ? "Normal weight"
                : bmi < 29.9
                    ? "Overweight"
                    : "Obese";

        setState(() {
          result = "Your BMI: ${bmi.toStringAsFixed(1)}\nCategory: $category";
        });
      }

      return Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: weightController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: 'Weight (kg)',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 10.0),
            TextField(
              controller: heightController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: 'Height (m)',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20.0),
            ElevatedButton(
              onPressed: calculateBMI,
              child: Text('Calculate BMI'),
              style: ElevatedButton.styleFrom(primary: Colors.green),
            ),
            SizedBox(height: 20.0),
            Text(
              result,
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 18.0, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      );
    },
  );
}
