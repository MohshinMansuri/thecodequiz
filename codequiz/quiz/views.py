from django.shortcuts import render, redirect
from .models import Submission, Results

CORRECT_ANSWERS = {
    'q1': 'Outputs data to the console',
    'q2': '_variable',
    'q3': '17',
    'q4': 'char',
    'q5': '15',
    'q6': '5',
    'q7': 'Both a and b',
    'q8': '4 bytes',
    'q9': 'scanf()',
    'q10': 'Both a and c',
    'q11': 'stdio.h',
    'q12': '// comment',
    'q13': 'int a = 10;',
    'q14': 'cout',
    'q15': 'A sequence of mutable values',
    'q16': 'for',
    'q17': 'Charles Babbage',
    'q18': 'Central Processing Unit',
    'q19': 'Linux',
    'q20': 'Random Access Memory',
    'q21': 'Microsoft',
    'q22': 'JavaScript',
    'q23': 'All of the above',
    'q24': 'Printer',
    'q25': 'Uniform Resource Locator',
    'q26': 'Hard Disk',
    'q27': 'Route data between networks',
    'q28': 'HyperText Transfer Protocol',
    'q29': 'dict = {1: \'one\', 2: \'two\'}',
    'q30': 'True',
    'q31': 'do-while loop',
    'q32': 'To exit a function',
    'q33': 'A method that initializes objects',
    'q34': 'All of the above',
    'q35': 'ROM',
    'q36': '15',
    'q37': 'Even',
    'q38': '1 2 3',
    'q39': '20',
    'q40': '7 3'
}


QUESTIONS = [
{
    'question': 'What does the print() function do in Python?',
    'options': ['Reads input', 'Outputs data to the console', 'Deletes data', 'Creates a loop'],
    'name': 'q1'
},
{
    'question': 'Which of the following is a valid variable name?',
    'options': ['1stVariable', '_variable', 'variable-name', 'var 1'],
    'name': 'q2'
},
{
    'question': 'What is the output of the following code: 2 + 3 * 5?',
    'options': ['25', '17', '15', '10'],
    'name': 'q3'
},
{
    'question': 'Which data type is used to create a variable that should store text in C?',
    'options': ['int', 'char', 'float', 'double'],
    'name': 'q4'
},
{
    'question': 'What will the following code print?',
    'code': ''' 
int a = 5, b = 10;
printf("%d", a + b);
            ''',
    'options': ['5', '10', '15', 'Error'],
    'name': 'q5'
},
{
    'question': 'What is the output of this C code?',
    'code': '''
int a = 4;
a++;
printf("%d", a);
            ''',
    'options': ['3', '4', '5', '6'],
    'name': 'q6'
},
{
    'question': 'Which of the following is a valid C declaration?',
    'options': ['int a, b;', 'float a, b;', 'Both a and b', 'None of the above'],
    'name': 'q7'
},
{
    'question': 'What is the size of an int data type in C on a 32-bit system?',
    'options': ['1 byte', '2 bytes', '4 bytes', '8 bytes'],
    'name': 'q8'
},
{
    'question': 'Which function is used to read input from the console in C?',
    'options': ['input()', 'get()', 'scanf()', 'cin'],
    'name': 'q9'
},
{
    'question': 'Which of the following loops is a pre-tested loop in C?',
    'options': ['for', 'do-while', 'while', 'Both a and c'],
    'name': 'q10'
},
{
    'question': 'Which header file is required to use printf and scanf?',
    'options': ['stdio.h', 'conio.h', 'math.h', 'string.h'],
    'name': 'q11'
},
{
    'question': 'Which of the following is used to create a single-line comment in C++?',
    'options': ['/* comment */', '// comment', '# comment', '<-- comment -->'],
    'name': 'q12'
},
{
    'question': 'Which of the following correctly declares a variable in C++?',
    'options': ['int a = 10;', 'int a : 10;', 'int a == 10;', 'int a - 10;'],
    'name': 'q13'
},
{
    'question': 'Which function is used to display output in C++?',
    'options': ['cin', 'cout', 'output', 'write'],
    'name': 'q14'
},
{
    'question': 'What is a list?',
    'options': ['A sequence of immutable values', 'A sequence of mutable values', 'A single value', 'None of the above'],
    'name': 'q15'
},
{
    'question': 'Which of the following is a loop in Python?',
    'options': ['repeat', 'for', 'if', 'else'],
    'name': 'q16'
},
{
    'question': 'Who is considered the father of computers?',
    'options': ['Alan Turing', 'Charles Babbage', 'Bill Gates', 'Steve Jobs'],
    'name': 'q17'
},
{
    'question': 'What does CPU stand for?',
    'options': ['Central Processing Unit', 'Control Program Unit', 'Compute Power Unit', 'Central Power Unit'],
    'name': 'q18'
},
{
    'question': 'Which of the following is an operating system?',
    'options': ['Python', 'Linux', 'HTML', 'HTTP'],
    'name': 'q19'
},
{
    'question': 'What does RAM stand for?',
    'options': ['Read Access Memory', 'Random Access Memory', 'Real Application Memory', 'Random Application Memory'],
    'name': 'q20'
},
{
    'question': 'Which company developed the Windows operating system?',
    'options': ['Google', 'Apple', 'Microsoft', 'IBM'],
    'name': 'q21'
},{
    'question': 'Which of the following is a programming language?',
    'options': ['HTML', 'CSS', 'JavaScript', 'SQL'],
    'name': 'q22'
},
{
    'question': 'What is the main function of the operating system?',
    'options': ['Manage files', 'Run programs', 'Control hardware', 'All of the above'],
    'name': 'q23'
},
{
    'question': 'Which of the following is not an input device?',
    'options': ['Keyboard', 'Mouse', 'Printer', 'Microphone'],
    'name': 'q24'
},
{
    'question': 'What is the full form of URL?',
    'options': ['Uniform Resource Locator', 'Universal Resource Locator', 'Uniform Retrieval Locator', 'Uniform Recognition Link'],
    'name': 'q25'
},
{
    'question': 'Which of the following storage devices typically has the largest capacity?',
    'options': ['Hard Disk', 'RAM', 'DVD', 'USB Flash Drive'],
    'name': 'q26'
},
{
    'question': 'What is the function of a router in a network?',
    'options': ['Store data', 'Route data between networks', 'Act as a firewall', 'None of the above'],
    'name': 'q27'
},
{
    'question': 'What does HTTP stand for?',
    'options': ['HyperText Transfer Protocol', 'HyperText Transport Program', 'HyperText Transmission Protocol', 'HyperText Translation Program'],
    'name': 'q28'
},
{
    'question': 'Which of the following is a valid way to declare a dictionary in Python?',
    'options': ['dict = {1: \'one\', 2: \'two\'}', 'dict = (1, 2)', 'dict = [1, 2]', 'dict = \'one\', \'two\''],
    'name': 'q29'
},
{
    'question': 'What will be the output of the following code?',
    'code': '''
x = 5
print(x == 5)
''',
    'options': ['True', 'False', 'Error', '5'],
    'name': 'q30'
},
{
    'question': 'Which loop will always execute at least once in C/C++?',
    'options': ['for loop', 'while loop', 'do-while loop', 'None'],
    'name': 'q31'
},
{
    'question': 'What is the purpose of the return statement in C/C++?',
    'options': ['To exit a function', 'To repeat a loop', 'To continue a loop', 'To terminate the program'],
    'name': 'q32'
},
{
    'question': 'What is a constructor in C++?',
    'options': ['A method that initializes objects', 'A method that destroys objects', 'A function to allocate memory', 'A class'],
    'name': 'q33'
},
{
    'question': 'Which of the following is used for creating an infinite loop in C++?',
    'options': ['while(true)', 'for(;;)', 'do {} while(true)', 'All of the above'],
    'name': 'q34'
},
{
    'question': 'Which of the following is a non-volatile memory?',
    'options': ['RAM', 'ROM', 'Cache', 'Registers'],
    'name': 'q35'
},
{
    'question': 'What will be the output of the following code?',
    'code': '''
#include <iostream>
using namespace std;
int main() {
    int a = 5, b = 10;
    int sum = a + b;
    cout << sum;
    return 0;
    }
''',
    'options': ['5', '10', '15', '20'],
    'name': 'q36'
},
{
    'question': 'What will be the output of the following code?',
    'code': '''
#include <iostream>
using namespace std;
int main() {
    int num = 8;
    if (num % 2 == 0) {
    cout << "Even";
            }     
    else {
        cout << "Odd";
        }
    return 0;
    }

''',
    'options': ['Even', 'Odd', '15', '20'],
    'name': 'q37'
},
{
    'question': 'What will be the output of the following code?',
    'code': '''
#include <iostream>
using namespace std;
int main() {
    for (int i = 1; i <= 3; i++) {
        cout << i << " ";
            }
    return 0;
}
''',
    'options': ['1 2 3', '1 2', '1', '2 3'],
    'name': 'q38'
},
{
    'question': 'What will be the output of the following code?',
    'code': '''
#include <iostream>
using namespace std;

int main() {
    int a = 20, b = 15;
    if (a > b) {
        cout << a;
    } else {
        cout << b;
    }
    return 0;
}
''',
    'options': ['15', '20', '0', 'Error'],
    'name': 'q39'
},
{
    'question': 'What will be the output of the following code?',
        'code': '''
#include <iostream>
using namespace std;
int main() {
    int x = 3, y = 7, temp;
    temp = x;
    x = y;
    y = temp;
    cout << x << " " << y;
    return 0;
}
''',
    'options': ['3 7', '7 3', '7 7', 'Error'],
    'name': 'q40'
}
]


def quiz_view(request):
    if request.method == 'POST':
        Submission.objects.create(
            enrollment_number = request.user.username,
            name=request.POST['name'],
            email=request.POST['email'],
            branch=request.POST['branch'],
            mobile=request.POST['mobile'],
        )
        return redirect('quiz/')
    return render(request, 'user_info.html')

def quiz(request):
    if request.method == 'POST':
        # Process the quiz submission
        form_data = request.POST
        score = 0
        answers = {}
        for key, correct_answer in CORRECT_ANSWERS.items():
            user_answer = form_data.get(key, "")
            if user_answer == correct_answer:
                score += 1
            answers[key] = user_answer
        Results.objects.create(
            enrollment_number = request.user.username,
            score = score,
            q1 = answers.get('q1'),
            q2 = answers.get('q2'),
            q3 = answers.get('q3'),
            q4 = answers.get('q4'),
            q5 = answers.get('q5'),
            q6 = answers.get('q6'),
            q7 = answers.get('q7'),
            q8 = answers.get('q8'),
            q9 = answers.get('q9'),
            q10 = answers.get('q10'),
            q11 = answers.get('q11'),
            q12 = answers.get('q12'),
            q13 = answers.get('q13'),
            q14 = answers.get('q14'),
            q15 = answers.get('q15'),
            q16 = answers.get('q16'),
            q17 = answers.get('q17'),
            q18 = answers.get('q18'),
            q19 = answers.get('q19'),
            q20 = answers.get('q20'),
            q21 = answers.get('q21'),
            q22 = answers.get('q22'),
            q23 = answers.get('q23'),
            q24 = answers.get('q24'),
            q25 = answers.get('q25'),
            q26 = answers.get('q26'),
            q27 = answers.get('q27'),
            q28 = answers.get('q28'),
            q29 = answers.get('q29'),
            q30 = answers.get('q30'),
            q31 = answers.get('q31'),
            q32 = answers.get('q32'),
            q33 = answers.get('q33'),
            q34 = answers.get('q34'),
            q35 = answers.get('q35'),
            q36 = answers.get('q36'),
            q37 = answers.get('q37'),
            q38 = answers.get('q38'),
            q39 = answers.get('q39'),
            q40 = answers.get('q40'),
        )
        return redirect('/quiz/thank-you/')
    return render(request, 'quiz.html', {'questions': QUESTIONS})

def thank_you(request):
    return render(request, 'thank_you.html')

def already_registered(request):
    return render(request, 'already_submitted.html')

def result(request):
    all_results = Results.objects.all()
    all_users = list(Submission.objects.all())
    return render(request, 'result.html', {'results' : all_results, 'all_users' : all_users})