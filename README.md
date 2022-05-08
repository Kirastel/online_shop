
## Main purpose:
This is online shop for buy 'Apple' products.


____
## Key concepts:
* Products for buying are added to the database by the admin;
* Every product have description and images;
* User can create order use froms on site;
* User can leave feedback for admin;
* Admin append and redact products image in admin-panel;
____
## Technical discription:

____

## To run application on local machine:
1. Clone the repository:
git clone https://github.com/Kirastel/online_shop.git && cd online_shop


2. Create a virtual environment:
python3 -m venv venv

3. Activate the virtual environment:
source venv/bin/activate

4. Install all required dependencies:
pip install -r requirements.txt

5. Collect static files:
python manage.py collectstatic

6. Apply the migrations:
python manage.py migrate

7. Create superuser:
python manage.py createsuperuser

8. Run server:
python manage.py runserver

9. From now local version is available at http://localhost:8000
