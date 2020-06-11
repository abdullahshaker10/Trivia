# Full Stack API Final Project

## Full Stack Trivia

In Trivia app you can start holding trivia in different fields and answer it if you can.you can list all questions, you can add a question in any field and you can play Trivia game in such field or in all fields together.

## Getting Started

### Pre-requisites and Local Development

Developers using this project should already have Python3, pip and node installed in their local machines.

### FrontEnd

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
npm start
```
### BackEnd

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
### Tests
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
## API Reference

### Getting Started
Base URL:At present this app can only run locally ans is not hosted as a base URL. The backend app is hosted at the defult 
```http://localhost:3000/```

### Error Handling
Errors are returned as json objects in hte format 
```
{
    'sucess' : False,
    'error' : 400,
    'message' : 'bad request'
}
```
The API will return three error types when requests fail:
    - 400: Bad Request
    - 404: Resource Not Found
    - 422: Not Processable
    
### Endpoints

### GET Categories
- General
    - Returns a dictionary of Categories object and sucess value.
- Sample ```http://localhost:3000/categories```
    
    ```
    {
       "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
        }, 
      "success": true
    }
   
    ```
### GET Questions

- General
    - Returns a list of Questions objects, object of categories, current category list, and sucess values.
    - Results are paginated in groups of 10.
- Sample ```http://localhost:3000/questions ```
    
    ```
    {
        "categories": {
          "1": "science", 
          "2": "art", 
          "3": "geography", 
          "4": "history", 
          "5": "entertainment", 
          "6": "sports"
        }, 
        
        "current_category": [5, 5, 5, 6, 6, 4, 3, 3, 3, 2],
        
        "questions": [
          {
            "answer": "Apollo 13", 
            "category": 5, 
            "difficulty": 4, 
            "id": 2, 
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
          }, 
          {
            "answer": "Tom Cruise", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
          }, 
   }
       ```
### DELETE Questions

- General
    - Returns a list of Questions objects without dleted object, count of questins, object of categories, current category list, and sucess values.
    - Results are paginated in groups of 10.

- Sample ```http://localhost:3000/questions/1 ```

   ```
    {
        "categories": {
          "1": "science", 
          "2": "art", 
          "3": "geography", 
          "4": "history", 
          "5": "entertainment", 
          "6": "sports"
        }, 
        
        "current_category": [5, 5, 5, 6, 6, 4, 3, 3, 3, 2],
        
        "questions": [
          {
            "answer": "Apollo 13", 
            "category": 5, 
            "difficulty": 4, 
            "id": 2, 
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
          }, 
          {
            "answer": "Tom Cruise", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
          }, 
   }
   
   ```
### POST Question

- General
    - Returns a list of Questions objects with new object, count of questins, object of categories, current   category list, and sucess values.
    - Results are paginated in groups of 10.

- Sample ```http://localhost:3000/questions ```
    
      ```
        {
        "categories": {
          "1": "science", 
          "2": "art", 
          "3": "geography", 
          "4": "history", 
          "5": "entertainment", 
          "6": "sports"
        }, 
        
        "current_category": [5, 5, 5, 6, 6, 4, 3, 3, 3, 2],
        
        "questions": [
          {
            "answer": "Apollo 13", 
            "category": 5, 
            "difficulty": 4, 
            "id": 2, 
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
          }, 
          {
            "answer": "new anser", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "new question"
          }, 
         }
   
     ```
    
### Start Quiz

- General
    - Returns a Question object, count of questins, object of categories, current category, difficulty, and sucess values.

- Sample ```http://localhost:3000/quizzes ```

    ```
    {
  "question": {
    "answer": "this", 
    "category": 1, 
    "difficulty": 1, 
    "id": 25, 
    "question": "this"
    }, 
    "success": true
  }

    ```
    
## Deployment N/A

## Authors N/A

## Achnowledgement N/A







