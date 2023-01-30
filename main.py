# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from dampy import AEM

class AEMClient:
    def __int__(self):
    # Getting started
    """
    By default, DamPy connects to AEM Author instance running locally with admin/admin as credentials.
    Keep your local AEM instance running when trying the above snippet.
    """
    author = AEM()

    # Import AEM from dampy


    # Create a handle to an AEM Instance
    def get_author(self, author):

        # List all assets in DAM
        author.dam.list()
    def create_aem_handle(self):
         # Create AEM handle to the given host and credentials
      aem = AEM(url, username, password)
        return aem

    def create_aem_default_handle(self):
         # Create AEM handle to default host, for admin user with password as â€˜new-passwordâ€™
       aem = AEM(password=<new - password>)
         return aem


def main():
    # Use a breakpoint in the code line below to debug your script.
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
