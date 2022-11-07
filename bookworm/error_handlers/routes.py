""" IMPORTS"""
from flask import Blueprint, render_template

error = Blueprint('error', __name__)


@error.app_errorhandler(400)
def handle_400(e):
    """
    400 ERROR FUNCTION
    Takes in 400 error and returns the error page with error message
    for 400 error
    """
    error_message = "It looks like this page was accessed incorrectly,\
        or may have be corrupted."
    return render_template(
        'error.html',
        error_number="400",
        error_message=error_message)


@error.app_errorhandler(401)
def handle_401(e):
    """
    401 ERROR FUNCTION
    Takes in 401 error and returns the error page with
    error message for 401 error
    """
    error_message = "It looks like you may not have authorisation\
        to view this page."
    return render_template(
        'error.html',
        error_number="401",
        error_message=error_message)


@error.app_errorhandler(404)
def handle_404(e):
    """
    404 ERROR FUNCTION - if address isn't right
    Takes in 404 error and returns the error page with
    error message for 404 error
    """
    error_message = "The page you're looking for couldn't be found.\
        Please check the page URL has been entered correctly"
    return render_template(
        'error.html',
        error_number="404",
        error_message=error_message)


@error.app_errorhandler(500)
def handle_500(e):
    """
    500 ERROR FUNCTION
    Takes in 500 error and returns the error page with error
    message for 500 error
    """
    error_message = "There was a problem while fulfilling your request."
    return render_template(
        'error.html',
        error_number="500",
        error_message=error_message)
