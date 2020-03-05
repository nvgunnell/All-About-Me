from tethys_sdk.base import TethysAppBase, url_map_maker


class Allaboutme(TethysAppBase):
    """
    Tethys app class for AboutNathan.
    """

    name = 'AboutNathan'
    index = 'allaboutme:home'
    icon = 'allaboutme/images/icon.gif'
    package = 'allaboutme'
    root_url = 'allaboutme'
    color = '#27ae60'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='allaboutme',
                controller='allaboutme.controllers.home'
            ),
            UrlMap(
                name='map',
                url='allaboutme/map',
                controller='allaboutme.contollers.map',
        )
        )

        return url_maps