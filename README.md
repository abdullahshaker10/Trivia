# Full Stack API Final Project

## Full Stack Trivia

In Trivia app you can start holding a trivia questions in different fields and answering it if you can.you can list all questions, you can add a question in any field and you can play Trivia game in such field or in all fields together.

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

#### GET '/categories'

   - Fetches a dictionary of categories in which the keys are the ids and the value 
     is the corresponding string of the category
   - Request Arguments: None
   - Returns: An object with a single key, categories, that contains 
     a object of id: category_string key:value pairs. 
    
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
#### GET '/questions'
   - Fetches all questions as objects, dictionary of categories, list of current categories,   
   - Request Arguments: None.
   - Return an object with keys categories, current_category, questions,
    total_questions and sucess value.
    
    
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
            "question": "What movie earned Tom Hanks his third straight 
            Oscar nomination, in 1996?"
          }, 
          {
            "answer": "Tom Cruise", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "What actor did author Anne Rice first denounce, 
            then praise in the role of her beloved Lestat?"
          }, 
            "success": true, 
            "total_questions": 34
      }
       ```
       
#### GET '/categories/1/questions'
   - Fetches all questions in given category   
   - Request Arguments: category id.
   - Return an object with keys categories, current_category, questions,
    total_questions and sucess value.
    
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
            "question": "What movie earned Tom Hanks his third straight 
            Oscar nomination, in 1996?"
          }, 
          {
            "answer": "Tom Cruise", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "What actor did author Anne Rice first denounce, 
            then praise in the role of her beloved Lestat?"
          }, 
            "success": true, 
            "total_questions": 34
       }
       ```
       
    

#### DELETE '/questions'
   - Delete a question with specific id.
   - Request Arguments: question's id.
   - Returns a object with keys Questions in which questions objects with new added question,
    count of questins, categories in which all categories, current category 
    in which list of current categories,and sucess values.
    
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
            "question": "What actor did author Anne Rice first denounce, 
            then praise in the role of her beloved Lestat?"
          }, 

        "success": true, 
        "total_questions": 34
     }
   
      ```
#### POST '/questions'
   - Create new question and add it to db.
   - Request Arguments:None.
   - Returns a object with keys Questions in which questions objects with new added question,
    count of questins, categories in which all categories, current category 
    in which list of current categories,and sucess values.
    
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
        "success": true, 
        "total_questions": 34
    }

 ```
    
#### GET '/quizzes'
   - Play a game to answer random questions of specific field or of all fields together. 
   - Request Arguments:None.
   - Returns object with keys Question for the current question and sucess for sucess values.
   
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







