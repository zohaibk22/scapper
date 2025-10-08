# Link Collector - Web Scraper GUI

A Django-based web application that provides a user-friendly graphical interface for web scraping and link collection. This tool allows users to extract and manage links from websites through an intuitive web interface.

## Features

- **Web Scraping Interface**: Easy-to-use GUI for scraping websites
- **Link Extraction**: Automatically extract and collect links from target URLs
- **Link Management**: Organize and manage collected links
- **Export Options**: Export collected data in various formats
- **User-Friendly Dashboard**: Clean and intuitive web interface
- **Batch Processing**: Process multiple URLs simultaneously

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd link_collector
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

## Usage

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000`
   - Use the web interface to start scraping websites

3. **Basic Operations**
   - Enter target URL(s) in the input field
   - Configure scraping parameters
   - Start the scraping process
   - View and manage collected links
   - Export results as needed

## Project Structure

```
link_collector/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── link_collector/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── scraper/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── templates/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── media/
```

## Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```

### Scraping Settings

Customize scraping behavior in `settings.py`:

```python
# Scraping configuration
SCRAPER_SETTINGS = {
    'USER_AGENT': 'Link Collector Bot 1.0',
    'DELAY': 1,  # Delay between requests (seconds)
    'TIMEOUT': 30,  # Request timeout
    'MAX_RETRIES': 3,
}
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with scraper interface |
| `/api/scrape/` | POST | Start scraping process |
| `/api/links/` | GET | Retrieve collected links |
| `/api/export/` | GET | Export links data |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development

### Running Tests

```bash
python manage.py test
```

### Code Style

This project follows PEP 8 style guidelines. Use flake8 for linting:

```bash
flake8 .
```

### Database Management

- **Create migrations**: `python manage.py makemigrations`
- **Apply migrations**: `python manage.py migrate`
- **Reset database**: `python manage.py flush`

## Deployment

### Production Setup

1. Set `DEBUG=False` in your environment
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Use a production WSGI server like Gunicorn

```bash
pip install gunicorn
gunicorn link_collector.wsgi:application
```

## Troubleshooting

### Common Issues

- **Port already in use**: Change the port with `python manage.py runserver 8080`
- **Database errors**: Run `python manage.py migrate` to apply migrations
- **Static files not loading**: Run `python manage.py collectstatic`

### Support

If you encounter any issues:

1. Check the [Issues](../../issues) page
2. Review the troubleshooting section
3. Create a new issue with detailed information

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Django web framework
- Uses Beautiful Soup for web scraping
- Bootstrap for responsive UI design
- Thanks to all contributors and the open-source community

## Changelog

### Version 1.0.0
- Initial release
- Basic web scraping functionality
- Django-based GUI interface
- Link extraction and management

---

**Note**: This is a development project. Use responsibly and respect website robots.txt files and terms of service.