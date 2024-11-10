import os
import unittest

from service.repository.file_repository import FileRepository

class MockModel:
    uid: int
    model_content: str

class TestFileRepository(unittest.TestCase):

    def __prepare_mock_object(self):
        mock_object = MockModel()
        mock_object.uid = 1
        mock_object.model_content = "Hello, World!"
        return mock_object

    def test_should_write_content_when_one_file_given(self):
        # given
        file_path = "test_file.txt"
        mock_repository = FileRepository(file_path, MockModel)
        mock_object = self.__prepare_mock_object()

        # when
        FileRepository.post(mock_repository, mock_object)

        # then
        try:
            with open(file_path, "r") as file:
                assert file.read() == '{"uid": 1, "model_content": "Hello, World!"}\n'
        finally:
            os.remove(file_path)

    def test_should_write_content_when_multiple_files_given(self):
        # given
        file_path = "test_file.txt"
        mock_repository = FileRepository(file_path, MockModel)
        mock_object = self.__prepare_mock_object()

        # when
        FileRepository.post(mock_repository, mock_object)
        FileRepository.post(mock_repository, mock_object)
        FileRepository.post(mock_repository, mock_object)
        FileRepository.post(mock_repository, mock_object)
        FileRepository.post(mock_repository, mock_object)

        # then
        try:
            with open(file_path, "r") as file:
                assert file.read() == ('{"uid": 1, "model_content": "Hello, World!"}\n'
                                       '{"uid": 2, "model_content": "Hello, World!"}\n'
                                       '{"uid": 3, "model_content": "Hello, World!"}\n'
                                       '{"uid": 4, "model_content": "Hello, World!"}\n'
                                       '{"uid": 5, "model_content": "Hello, World!"}\n')
        finally:
            os.remove(file_path)

    def test_should_get_all_content(self):
        # given
        file_path = "test_file.txt"
        mock_repository = FileRepository(file_path, MockModel)
        mock_object = self.__prepare_mock_object()

        # when
        try:
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)

            with open(file_path, "r") as file:
                assert file.read() == ('{"uid": 1, "model_content": "Hello, World!"}\n'
                                       '{"uid": 2, "model_content": "Hello, World!"}\n'
                                       '{"uid": 3, "model_content": "Hello, World!"}\n'
                                       '{"uid": 4, "model_content": "Hello, World!"}\n'
                                       '{"uid": 5, "model_content": "Hello, World!"}\n')


            get_all_content = FileRepository.get_all(mock_repository)

            # then
            assert len(get_all_content) == 5
            assert get_all_content[0]['uid'] == 1
            assert get_all_content[1]['uid'] == 2
            assert get_all_content[2]['uid'] == 3
            assert get_all_content[3]['uid'] == 4
            assert get_all_content[4]['uid'] == 5

        finally:
            os.remove(file_path)

    def test_should_get_content_by_uid(self):
        # given
        file_path = "test_file.txt"
        mock_repository = FileRepository(file_path, MockModel)
        mock_object = self.__prepare_mock_object()

        # when
        try:
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)

            get_by_uid_ = FileRepository.get(mock_repository, 3)
            get_all_content = FileRepository.get(mock_repository, 4)

            # then
            assert get_by_uid_['uid'] == 3
            assert get_all_content['uid'] == 4
            assert get_by_uid_['model_content'] == "Hello, World!"
            assert get_all_content['model_content'] == "Hello, World!"

        finally:
            os.remove(file_path)

    def test_should_delete_content(self):
        # given
        file_path = "test_file.txt"
        mock_repository = FileRepository(file_path, MockModel)
        mock_object = self.__prepare_mock_object()

        # when
        try:
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)
            FileRepository.post(mock_repository, mock_object)

            FileRepository.delete(mock_repository, 1)
            FileRepository.delete(mock_repository, 2)
            FileRepository.delete(mock_repository, 3)
            FileRepository.delete(mock_repository, 4)

            # then
            with open(file_path, "r") as file:
                assert file.read() == ('{"uid": 5, "model_content": "Hello, World!"}\n')

        finally:
            os.remove(file_path)


    def test_should_raise_exception_when_invalid_file_path_given(self):
        # given
        invalid_file_path = "/invalid/path/test_file.txt"

        mock_repository = FileRepository(invalid_file_path, MockModel)

        # when
        call_get = lambda: mock_repository.get_all()

        # when
        with self.assertRaises(Exception):
            call_get()