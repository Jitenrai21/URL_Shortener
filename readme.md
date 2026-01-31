# Django URL Shortener

A full-featured URL shortening service built with Django, providing user authentication, link management, analytics, and advanced features like QR code generation and expiration time control.

## Demo Video

Watch a complete demonstration of the application features:

<div align="center">
  <img src="https://github.com/Jitenrai21/URL_Shortener/blob/main/demo_vid/demo.gif" alt="Demo" width="1280"/>
</div>

The demo showcases the complete workflow including user registration, URL shortening, management features, analytics dashboard, QR code generation, and expiration time configuration.

## Features

### Core Features
- **URL Shortening**: Convert long URLs into short, shareable links using Base62 encoding
- **User Authentication**: Secure registration, login, and logout functionality
- **URL Management**: View, edit, and delete your shortened URLs
- **Analytics Dashboard**: Track click counts and monitor link performance
- **Active/Inactive Toggle**: Enable or disable URLs without deleting them

### Advanced Features
- **Custom Short Keys**: Option to create custom memorable short URLs
- **Expiration Time**: Set automatic expiration dates for temporary links
- **QR Code Generation**: Generate downloadable QR codes for each shortened URL
- **User-Specific URLs**: Each user manages their own collection of shortened URLs

## Technology Stack

- **Backend**: Django 4.x
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Forms**: django-crispy-forms with Bootstrap 5
- **QR Code**: qrcode library with Pillow
- **Frontend**: HTML5, CSS3, Bootstrap 5

## Installation Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Url_shortener
   ```

2. **Create and activate virtual environment**
   
   Windows:
   ```bash
   python -m venv env
   .\env\Scripts\activate
   ```
   
   Linux/Mac:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## Usage Instructions

### Getting Started

1. **Register an Account**
   - Navigate to the registration page
   - Provide username, email, and password
   - Confirm your password and submit

2. **Login**
   - Use your credentials to access your dashboard

3. **Shorten a URL**
   - Enter the long URL you want to shorten
   - Optionally provide a custom short key
   - Set an expiration date if needed (optional)
   - Click "Shorten URL"

4. **Manage Your URLs**
   - View all your shortened URLs on the dashboard
   - Click "Details" to see analytics and QR code
   - Use "Edit" to modify the original URL or expiration time
   - Use "Delete" to remove a shortened URL
   - Toggle active/inactive status as needed

5. **Generate QR Codes**
   - Navigate to the URL details page
   - View the generated QR code
   - Download the QR code for sharing

6. **Share Your Short URLs**
   - Copy the shortened URL from your dashboard
   - Share it via any platform
   - Track clicks and engagement through analytics

### Advanced Features

- **Custom Short Keys**: When creating a URL, provide a custom key instead of using auto-generated ones
- **Expiration Time**: Set a date and time when the link should stop working
- **Edit URLs**: Update the original URL or modify expiration settings after creation
- **QR Code Download**: Save QR codes locally for offline use

## Folder Structure

```
URL_Shortener/
│
├── url_shortener/                 # Main project settings (matches your folder)
│   ├── settings.py                # Django configuration
│   ├── urls.py                    # Root URL routing
│   ├── wsgi.py                    # WSGI application entry
│   └── asgi.py                    # ASGI application entry
│
├── shortenerApp/                  # URL shortener application
│   ├── __init__.py
│   ├── admin.py                   # Admin panel configuration
│   ├── apps.py
│   ├── forms.py                   # Form definitions
│   ├── models.py                  # Database models (ShortURL)
│   ├── tests.py
│   ├── utils.py                   # Helper functions (Base62 encoding, etc.)
│   ├── views.py                   # View functions and logic
│   └── urls.py                    # App-specific URL patterns (recommended to add)
│
├── templates/                     # HTML templates
│   ├── base.html                  # Base template with navigation
│   ├── home.html                  # Dashboard and URL list
│   ├── registration/              # Authentication templates
│   │   ├── login.html
│   │   └── register.html
│   └── shortener/                 # URL management templates
│       ├── create_url.html
│       ├── delete_url.html
│       ├── edit_url.html
│       └── url_detail.html
│
├── static/                        # Static files (CSS, JS, images)
│   └── css/
│       └── style.css
│
├── media/                         # User-uploaded files
│
├── demo_vid/                      # Demo video folder
│   └── demo.mp4
│
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation

```

## Key Components

### Models
- **ShortURL**: Stores original URLs, short keys, user associations, click counts, active status, and expiration timestamps

### Views
- User authentication (register, login, logout)
- URL creation and shortening
- URL listing and management
- URL details with analytics and QR code
- Redirect handling with click tracking

### Forms
- **URLShortenForm**: Handles URL input, custom keys, and expiration settings
- Authentication forms for registration and login

## Contributing

Contributions are welcome to improve the Django URL Shortener project. To contribute:

1. **Fork the repository**
   - Create your own fork of the project

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clean, documented code
   - Follow Django best practices
   - Test your changes thoroughly

4. **Commit your changes**
   ```bash
   git commit -m "Add: description of your feature"
   ```

5. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Submit a pull request**
   - Provide a clear description of your changes
   - Reference any related issues

### Contribution Guidelines
- Follow PEP 8 style guidelines for Python code
- Write meaningful commit messages
- Include comments for complex logic
- Update documentation as needed
- Test all functionality before submitting

## License

This project is open source and available under the MIT License.

## Future Enhancements

Potential features for future development:
- Link grouping and categorization
- Bulk URL shortening
- API endpoints for third-party integration
- Advanced analytics with charts and graphs
- Custom domains support
- Password-protected URLs
- URL preview before redirect

## Acknowledgments

Built with Django and modern web technologies to provide a robust and scalable URL shortening solution.
