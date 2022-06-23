"""Portal settings tests."""
from kitconcept import api
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING  # noqa: E501

import unittest


class TestPortalSettings(unittest.TestCase):
    """Test that Portal configuration is correctly done."""

    layer = PORTAL_UFT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]

    def test_portal_title(self):
        """Test portal title."""
        value = api.portal.get_registry_record("plone.site_title")
        expected = "Portal UFT Exercicio8"
        self.assertEqual(value, expected)

    def test_portal_timezone(self):
        """Testa se o timezone está correto."""
        value = api.portal.get_registry_record("plone.portal_timezone")
        expected = "America/Araguaina"
        self.assertEqual(value, expected)

    def test_portal_sitemap(self):
        """Testa se o sitemap está habilitado."""
        value = api.portal.get_registry_record("plone.enable_sitemap")
        self.assertTrue(value)

    def test_portal_email_address(self):
        """Valida o endereço de email do portal."""
        value = api.portal.get_registry_record("plone.email_from_address")
        expected = "paulorogerio@uft.edu.br"
        self.assertEqual(value, expected)

    def test_portal_email_name(self):
        """Valida o nome usado pelo email do portal."""
        value = api.portal.get_registry_record("plone.email_from_name")
        expected = "Portal UFT Exercicio8"
        self.assertEqual(value, expected)
