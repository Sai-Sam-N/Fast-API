# Fast-API
Refer : https://youtube.com/playlist?list=PLZoTAELRMXVPgsojPOHF9i0u2L83-m9P7&amp;si=3yc_H4u3Im4BgWBc

### Introduction
* ML models when deployed to cloud --> Flask framework was used. 
* Flask framework - can deploy, create frontend, create an API and expose it to the frontend application.

### FastAPI
Refer : https://fastapi.tiangolo.com/

* FastAPI - also a framework like Flask and Django. Actually, its better. Django is huge & covers a lot of functionalities (downside - huge) which is addressed by FastAPI. Flask has very less number of features so FastAPI is better than Flask too. So its like: <br>
<--- Flask (Light weight) -------------- FastAPI ------------------- Django (Heavy) ----> <br>
* FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
* Its fast due to a property called [ASGI](https://asgi.readthedocs.io/en/latest/) (Asynchronous Server Gateway Interface). Flask and Django use [WSGI](https://wsgi.readthedocs.io/en/latest/what.html) (Web Server Gateway Interface). Difference between ASGI and WSGI is that ASGI is Asynchronous & WSGI is Synchronous. 
* FastAPI uses [Pydantic](https://docs.pydantic.dev/latest/) - Data Validation and settings management using python type annotations. Hence, it enforces type hints at runtime and provides user friendly errors when data is invalid.
    - From the front end we want to send parameters and do a post request. While doing a post request using using the requests library, I can capture the values coming in the post. Similarly, this library does the work of the request object itself and apart from that it has additional functionalities. 
* FastAPI also uses Starlette
* Swagger - a json schema. Now known as OpenAPI. If JSON Schema given as a XML file, it can be loaded and we can see the different APIs there. 
* Has a similar code to Flask.

### uvicorn
* used for the ASGI server implementation.

<b>Kite</b> - nice extension that provides suggestions - can be integrated with VSCode, Spyder, etc.

#### Virtual Environment details
![alt text](image.png) <br>
Activating the virtual environment: FastAPI_env
![alt text](image-1.png) <br>
Trying to deactivate the virtual environment :
![alt text](image-2.png)

#### Installations:
![alt text](image-3.png)

### Asynchronous and Synchronous (differences and details)

<----- Notes ----->

