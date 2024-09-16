from django.test import TestCase

from taxi.forms import (
    DriverCreationForm,
    DriversSearchForm,
    CarsSearchForm,
    ManufacturerSearchForm
)


class FormsTest(TestCase):
    def test_driver_creation_form_with_license_number_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "test first",
            "last_name": "test last",
            "license_number": "TES12345",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_drivers_search_form(self):
        form_data = {"username": "testuser"}
        form = DriversSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "testuser")

    def test_car_search_form(self):
        form_data = {"model": "test"}
        form = CarsSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["model"], "test")

    def test_manufacturer_search_form(self):
        form_data = {"name": "test"}
        form = ManufacturerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "test")
