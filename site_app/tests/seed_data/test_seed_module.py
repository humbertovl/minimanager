from importlib import import_module
from importlib.util import find_spec

from django.conf import settings
from django.test import TestCase


class SeedModuleTestCase(TestCase):
    def setUp(self) -> None:
        self.module_name = settings.APP_SEEDER_MODULE_NAME

    def test_seeder_module_exists(self) -> None:
        check_module = find_spec('site_app.data.' + self.module_name)
        self.assertIsNotNone(
            check_module,
            f'Missing module: site_app.data.{self.module_name}'
        )

    def test_seeder_implements_all_abs_methods(self) -> None:
        seeder_module = import_module('site_app.data.' + self.module_name)
        # __abstract_methods__ is supposed to give empty frozenset
        # if all abs methods are implemented
        missing_abs_methods: str = ', '.join(seeder_module.DataSeeder.__abstractmethods__)
        self.assertEqual(
            len(missing_abs_methods),
            0, # if no missing methods then should empty string
            f'Following methods are not implemented: {missing_abs_methods!s}',
        )
