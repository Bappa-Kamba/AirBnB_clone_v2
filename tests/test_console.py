import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from models.base_model import BaseModel
from models.__init__ import storage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()
        self.base_model = BaseModel()

    def tearDown(self):
        storage._FileStorage__objects = {}

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Test help command"""
        self.console.onecmd("help")
        self.assertIn("Documented commands (type help <topic>):", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        """Test quit command"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        """Test EOF command"""
        with patch('builtins.input', return_value='EOF'):
            self.console.cmdloop()
            self.assertEqual("\n", mock_stdout.getvalue())

    def test_do_create(self):
        """Test create command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

            self.console.onecmd("create BaseModel name='test'")
            self.assertIn("BaseModel", storage.all())
            self.assertIn("test", str(storage.all()["BaseModel.test"].__dict__.values()))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """Test show command"""
        self.base_model.save()
        self.console.onecmd("show BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

        self.console.onecmd("show BaseModel 12345")
        self.assertIn("** no instance found **", mock_stdout.getvalue())

        self.console.onecmd(f"show BaseModel {self.base_model.id}")
        self.assertIn(str(self.base_model), mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        """Test destroy command"""
        self.base_model.save()
        self.console.onecmd("destroy")
        self.assertIn("** class name missing **", mock_stdout.getvalue())

        self.console.onecmd("destroy BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

        self.console.onecmd("destroy BaseModel 12345")
        self.assertIn("** no instance found **", mock_stdout.getvalue())

        self.console.onecmd(f"destroy BaseModel {self.base_model.id}")
        self.assertNotIn(self.base_model.id, storage.all())

    # Additional test cases for other commands can be added similarly

if __name__ == '__main__':
    unittest.main()