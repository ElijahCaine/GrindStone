#!/usr/bin/env python
"""
File: lib.py
Package: grindstone
Author: Elijah Caine
Description:
    Utility functionality and classes for the grindstone package.
"""
import unittest
import os
import shutil
import json

class GrindStone(object):
    """
    The GrindStone object.
    """
    def __init__(self):
        # Establish variables
        self.grindstone_filename = '/.grindstone'
        self.cwd = os.getcwd()
        self.home = os.environ['HOME']

        # set the path
        self.grindstone_path = self.grindstone_location()
        # open the grindstone
        self.grindstone = self.open_grindstone()
        # write the grindstone
        #self.write_grindstone()


    def grindstone_location(self):
        """
        Returns verified location of `.grindstone` file if it exist in
            the current working directory or HOME.
        Returns None otherwise.
        """
        # If there is a grindstone file in the cwd,
        if os.path.isfile(self.cwd + self.grindstone_filename):
            # return that file path
            return self.cwd + self.grindstone_filename
        else:
            # Otherwise default to home directory
            return self.home + self.grindstone_filename


    def open_grindstone(self):
        """
        Opens a grindstone file and populates the grindstone with it's
        contents.
        """
        with open(self.grindstone_path, 'a+') as f:
            try:
                # Try opening the file
                return json.loads(f.read())
            # If the file is empty
            except json.decoder.JSONDecodeError:
                # Default return empty object with empty tasks list
                return {'tasks': []}


    def add_task(self, name=None, desc=None):
        """
        Adds object to list of grindstone['tasks'].
        """
        if name is not None:
            to_add = {name: desc}
            self.grindstone['tasks'].append(to_add)
        else:
            raise ValueError('Tasks `name` cannot be None')


    def delete_task(self, task=None):
        """
        Deletes a given task by name.
        """
        pass


    def write_grindstone(self):
        """
        Writes self.gs to self.grindstone_path.
        """
        with open(self.grindstone_path, 'w') as f:
            # Write the JSON dump of the file
            f.write(json.dumps(self.grindstone))


class TestGrindStoneLibrary(unittest.TestCase):

    def setUp(self):
        self.testing_path = '/tmp/grindstone_testing'

        os.environ['HOME'] = self.testing_path
        try:
            os.mkdir(self.testing_path)
        except FileExistsError:
            shutil.rmtree(self.testing_path)
            os.mkdir(self.testing_path)
        os.chdir(self.testing_path)


    def tearDown(self):
        os.remove(self.gs.grindstone_path)
        shutil.rmtree(self.testing_path)


    def test_cwd_path(self):
        os.mkdir('./t')
        os.chdir('./t')
        open('.grindstone', 'w').close()
        self.gs = GrindStone()
        self.assertEqual(self.gs.grindstone_path,\
                         os.path.realpath('.grindstone'))


    def test_home_path(self):
        self.gs = GrindStone()
        self.assertEqual(self.gs.grindstone_path,\
                         os.path.realpath(os.environ['HOME']+'/.grindstone'))


    def test_add_one_complete_task(self):
        self.gs = GrindStone()
        self.gs.add_task('book1', 'read the book')
        self.assertEqual(self.gs.grindstone,\
                         {'tasks': [{'book1': 'read the book'}]})

        self.gs.write_grindstone()
        with open(self.gs.grindstone_path, 'r') as f:
            file_contents = f.read()
        self.assertEqual(file_contents,\
                         '{"tasks": [{"book1": "read the book"}]}')


    def test_add_one_shallow_task(self):
        self.gs = GrindStone()
        self.gs.add_task('bookA')
        self.assertEqual(self.gs.grindstone, {'tasks': [{'bookA': None}]})

        self.gs.write_grindstone()
        with open(self.gs.grindstone_path, 'r') as f:
            file_contents = f.read()
        self.assertEqual(file_contents,\
                         '{"tasks": [{"bookA": null}]}')


    def test_add_complete_tasks(self):
        self.gs = GrindStone()
        self.gs.add_task('book1', 'read the book')
        self.gs.add_task('book2', 'read the other book')
        self.assertEqual(self.gs.grindstone,\
                         {'tasks': [{'book1': 'read the book'},\
                         {'book2': 'read the other book'}]})


        self.gs.write_grindstone()
        with open(self.gs.grindstone_path, 'r') as f:
            file_contents = f.read()
        self.assertEqual(file_contents,\
                         '{"tasks": [{"book1": "read the book"}, '+
                         '{"book2": "read the other book"}]}')

    def test_add_empty_task(self):
        self.gs = GrindStone()
        with self.assertRaises(ValueError):
            self.gs.add_task(desc='foo')


    def test_add_task_with_no_name(self):
        self.gs = GrindStone()
        pass


if __name__ == '__main__':
    unittest.main()
