ReStyle – Marketplace Web Application
A full-stack web application for buying and selling second-hand clothing items. Users can register, post listings, browse items, save favorites, add products to cart, and message other users.
Built with Python and Django as a personal project during the Software Development Academy program.

Features
User Authentication – Register, log in, and log out with session management
Product Listings – Create and view detailed clothing listings with images
Browse & Search – Browse all items, filter by category, and search
Favorites – Save items to a personal favorites list
Shopping Cart & Checkout – Add items to cart and proceed to checkout
Inbox / Messaging – Internal messaging system between users
Media Uploads – Product images stored and served via Django media files

Tech Stack
Layer              Technology   
Backend            Python 3, Django
Database           SQLite (Django ORM)
Frontend           HTML, CSS
Media              Django media files
Version Control    Git, GitHub


RESTYLE_DJANGO/
├── products/                   # Product listings, cart, favorites, search
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── context_processors.py
│   └── admin.py
├── users/                      # User authentication and profiles
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── ReStyle_DjangoProject/      # Django project settings
│   ├── settings.py
│   └── urls.py
├── templates/                  # HTML/CSS templates
│   ├── home.html
│   ├── ad_list.html
│   ├── ad_detail.html
│   ├── add_product.html
│   ├── favorites_list.html
│   ├── cart.html
│   ├── checkout.html
│   ├── inbox.html
│   ├── search.html
│   └── users/
├── static/                     # Static images
│   └── images/
├── media/images/               # User-uploaded product images
├── db.sqlite3
└── manage.py
