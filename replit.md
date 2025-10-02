# Flask Web Application

## Overview

This is a modern Flask web application that demonstrates a clean, well-structured approach to building web applications with Python. The application features a responsive multi-page website with home, about, and contact pages, built using Flask as the backend framework and Bootstrap for the frontend styling. The application includes proper error handling, form processing, and follows Flask best practices for template organization and routing.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templating system with template inheritance
- **Base Template Pattern**: Uses `base.html` as the foundation template with block content inheritance
- **CSS Framework**: Bootstrap 5 with dark theme via Replit CDN integration
- **Icons**: Font Awesome 6.4.0 for consistent iconography
- **Responsive Design**: Mobile-first approach with Bootstrap's grid system
- **Custom Styling**: Additional CSS in `static/style.css` for hover effects and custom enhancements

### Backend Architecture
- **Framework**: Flask (Python micro-framework)
- **Application Structure**: Single-file application (`app.py`) with clear separation of concerns
- **Routing**: RESTful route organization with GET/POST method handling
- **Error Handling**: Custom 404 and 500 error handlers with user-friendly error pages
- **Session Management**: Flask sessions with configurable secret key
- **Form Processing**: Server-side form validation and flash messaging system

### Application Flow
- **Entry Point**: `main.py` serves as the application runner
- **Route Handlers**: Individual functions for each page (index, about, contact)
- **Template Rendering**: Dynamic content injection through Jinja2 templates
- **Static Assets**: CSS and potential JS files served from `/static` directory

### Security Considerations
- **Secret Key**: Environment-based session secret with fallback for development
- **Form Validation**: Server-side input validation for contact form
- **Error Logging**: Structured logging for debugging and monitoring

### Development Features
- **Debug Mode**: Enabled for development with detailed error reporting
- **Hot Reload**: Flask development server with automatic reloading
- **Logging**: Configurable logging levels for debugging

## External Dependencies

### Frontend Dependencies
- **Bootstrap CSS**: `https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css` - UI framework with dark theme
- **Font Awesome**: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css` - Icon library

### Python Dependencies
- **Flask**: Core web framework for routing, templating, and request handling
- **Werkzeug**: WSGI utilities (included with Flask)
- **Jinja2**: Template engine (included with Flask)

### Infrastructure
- **Host Configuration**: Configured to run on `0.0.0.0:5000` for Replit compatibility
- **Environment Variables**: `SESSION_SECRET` for production security
- **Static File Serving**: Flask's built-in static file serving for CSS/JS assets

### Form Processing
- **Contact Form**: Basic form handling with name, email, and message fields
- **Flash Messaging**: User feedback system for form submissions and validation errors
- **Redirect Pattern**: Post-redirect-get pattern for form submission handling

Note: The application currently handles form data in memory only. For production use, integration with a database system and email service would be recommended for the contact form functionality.