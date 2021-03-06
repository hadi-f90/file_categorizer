import os

from . import logger
import config


# =============directory definitions=================
class folder:
    def __init__(self, current_directory=os.getcwd()[:]):
        # Setting and checking the directory
        self.current_dir = current_directory
        logger.log.info(f'Trying to set address to: {self.current_dir}')

        try:
            assert os.path.isdir(self.current_dir)
        except AssertionError:
            logger.log.critical(
                f'{self.current_dir} either is not a directory or doesn\'t exist. Check it!')

    # Appending path to file/folder name function
    def walker(self, n=False,):
        """Walks through directory to return
        append the full adrress to each file

        Yields:
            [str]: [full path of file]
        """
        for root, dirs, files in os.walk(self.current_dir, topdown=False):
            if len(files) != 0:
                for _ in files:
                    self.selected_file_name = _
                    yield os.path.join(root, _)

        if n is True:
            self.walker()

    def dir_walker(self, n=False):
        """Walks through directory to return
        append the full adrress to each folder

        Yields:
            [str]: [full path of file]
        """
        for root, dirs, files in os.walk(self.current_dir, topdown=n):
            if len(files) != 0:
                for _ in dirs:
                    self.selected_dir_name = _
                    yield os.path.join(root, _)

    def mkdir(self, sub_dir):
        """Creates a series of directorys from a given list/tuple/set"""
        try:
            logger.log.info(f'Creating {self.current_dir} if not exist...')
            os.makedirs(sub_dir)

        except OSError:
            logger.log.info(f'Using it the existing {sub_dir} directory...')

    def delete(self, sub_dir):
        try:
            logger.log.info(f'Checking if {sub_dir} exists...')
            assert os.path.exists(sub_dir)
            logger.log.warning(f'Removing {sub_dir}...')
            os.rmdir(sub_dir)
            logger.log.info(f'{sub_dir} Removed successfully!')

        except AssertionError:
            logger.log.warning(f'{sub_dir} was not a directory.')

    def __str__(self) -> str:
        return self.current_dir


class destination_folder(folder):
    def __init__(self,
                 input_dir=os.getcwd()):
        super().__init__()
        # preparing destination path
        # self.mkdir(os.getcwd()+'/Categories/')
        self.current_dir = f'{os.getcwd()} /Categories/' \
            if input_dir in ('', None) else input_dir
        # print(self.current_dir)
        if os.path.exists(self.current_dir):
            logger.log.info(f'Using already existing \
                {self.current_dir} directory.')

        else:
            os.mkdir(self.current_dir)
            logger.log.info(f'Creating {self.current_dir}')

        os.chdir(self.current_dir)
        logger.log.info(f'destination set to dir: {self.current_dir}')
        # print(self.current_dir)

        self.category_dirs = {}
        # print(self.category_dirs)

    def add_category(self, category_name):
        self.category_dirs[category_name] = \
            self.current_dir + category_name
        # print(self.category_dirs)
        if os.path.exists(self.category_dirs[category_name]):
            logger.log.info(f'Using the existing \
                {self.category_dirs[category_name]}')
        else:
            self.mkdir(self.category_dirs[category_name])
            logger.log.info(f'{category_name} directory structure created.')

    def __dict__(self):
        return self.category_dirs
