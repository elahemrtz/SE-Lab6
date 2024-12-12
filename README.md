## آزمایش ششم: استقرار با استفاده از  داکر
# سرورها
برای سرورها یک
API
ساده با استفاده از چاروب
Flask
ساختیم. فایل‌های این قسمت در پوشه‌ی
backend/
ثرار گرفتند.
داکرفایل بک‌اند هم داخل همین پوشه قرار دارد.
مهم‌ترین APIهای این قسمت عبارتند از
```
GET /healthcheck        <--- Simple Healthcheck 
POST /set_var           <--- Create a key/value variable in database
GET /get_var            <--- Retrieve a variable value from database by its key
PUT /edit_var           <--- Edit a variable's value in database by its key
DELETE /delete_var      <--- Delete a variable from database by its key
```
سرور ما به کانتینر 
database
که جلوتر توضیح داده می‌شود وصل میشود و امکان انجام عملیات‌های ساده 
CRUD
را به ما می‌دهد.
سرور از طریق یک سری 
Environment Variable
که در فایل داکر-کومپوز در اختیار گرفته به دیتابیس وصل میشود و این عملیات را انجام میدهد. کتابخانه‌ی 
psycopg
به عنوان واسط برای اتصال به سرور استفاده شده است.

محتویات داکرفایل این قسمت بصورت زیر است.
```dockerfile
FROM python:3.11-alpine

WORKDIR backend

COPY backend/requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENV FLASK_APP=backend/app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

COPY backend .

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]
```
در این فایل ابتدا 
python:3.11
را
pull
میکنیم. سپس 
cwd
را پوشه‌ی
backend
قرار می‌دهیم و فایل 
requirements.txt
را به کنتینر کپی کرده و کتابخانه‌ها را
install 
میکنیم. سپس تعدادی متغیر محیطی را مقداردهی میکنیم و سایر فایل‌ها را کپی میکنیم. در نهایت پورت ۵۰۰۰ را 
Expose
میکنیم و دستور اجرای برنامه را اجرا میکنیم.