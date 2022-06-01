**For getting the User details**
http://localhost:8000/api/accounts/users/me/

**For User Signup Verify**
http://127.0.0.1:8000/api/accounts/signup/verify/?code=<code>

**For User SignUp**
http://127.0.0.1:8000/api/accounts/signup/

**For User Login**
http://127.0.0.1:8000/api/accounts/login/

**For Password Reset**
http://127.0.0.1:8000/api/accounts/password/reset/

**For Adding Item**
http://127.0.0.1:8000/api/store/add_item/
POST request (Only data) fields = ('title', 'desc', 'featured', 'price', 'seller_id', 'category') Token Required

**For Adding Item Images**
http://127.0.0.1:8000/api/store/add_item_images/
POST request (Only data) fields =('item_id', 'itemImage') Token Required

**For Getting Items**
http://127.0.0.1:8000/api/store/list/
GET Request

**For Updating Item**
PUT Request, (Query Parameters, id, seller_id) id is item table primary key
Data = (Update fields) Header Token Required

**For Deleting Item**
DELETE Request, (Query Parameters, seller_id)
Request data: id Item table primary key
Token in Header Required