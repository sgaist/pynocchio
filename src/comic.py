# -*- coding: UTF-8 -*-

from rar_loader import *
from zip_loader import *
from tar_loader import *
from folder_loader import *

import collections
from PySide.QtCore import QObject


class Comic(QObject):

    Pages = collections.namedtuple('Page', 'data title')

    def __init__(self, name, path, pages, titles, parent=None):

        super(Comic, self).__init__(parent)

        self.name = name
        self.path = path
        self.current_page_index = 0
        self.page_data = self.Pages(pages, titles)

    # def load(self, filename):
    #
    #     if ZipLoader.is_zip_file(filename):
    #
    #         if not self._load_content(ZipLoader(), filename):
    #             print self.tr('failed open comic!')
    #
    #         return True
    #
    #     elif RarLoader.is_rar_file(filename):
    #
    #         if not self._load_content(RarLoader(), filename):
    #             print self.tr('failed open comic!')
    #
    #         return True
    #
    #     elif TarLoader.is_tar_file(filename):
    #
    #         if not self._load_content(TarLoader(), filename):
    #             print self.tr('failed open comic!')
    #
    #         return True
    #
    #     self.tr('A error ocurred in open comic file!')
    #
    #     # QMessageBox.information(self, self.tr('Error'), self.tr("File type is not supported!!"))
    #
    #     return False

    # def load_folder(self, folder_name):
    #
    #     if FolderLoader.is_folder(folder_name):
    #         return self._load_content(FolderLoader(), folder_name)
    #
    #     print 'Not is folder'
    #     return False
    #
    # def _load_content(self, loader, file_name):
    #
    #     pages, titles, self.path, self.name = loader.load_file(file_name)
    #
    #     if len(pages) == 0:
    #         return False
    #
    #     self.page_data = self.Pages(pages, titles)
    #     self.current_page_index = 0
    #
    #     return True

    def get_current_page(self):

        if self.page_data is not None:
            return self.page_data.data[self.current_page_index]

        return None

    def get_current_page_title(self):

        if self.page_data is not None:
            return self.page_data.title[self.current_page_index]

        return None

    def go_next_page(self):

        range_list = range(0, self.get_number_of_pages() - 1)

        if self.current_page_index in range_list:
            self.current_page_index += 1

    def go_previous_page(self):

        range_list = range(1, self.get_number_of_pages())

        if self.current_page_index in range_list:
            self.current_page_index -= 1

    def go_first_page(self):
        self.current_page_index = 0

    def go_last_page(self):
        self.current_page_index = self.get_number_of_pages() - 1

    def set_current_page_index(self, idx):

        if idx in range(0, self.get_number_of_pages()):
            self.current_page_index = idx

    def get_number_of_pages(self):
        return len(self.page_data.data)
