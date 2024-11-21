{
    'name': 'Game Library',
    'version': '0.1',
    'summary': 'Manage games and user libraries like Steam',
    'author': 'NHBKhang',
    'category': 'Entertainment',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/game_library_security.xml',
        'security/game_game_security.xml',
        'security/game_genre_security.xml',
        'security/game_release_report_security.xml',

        'report/game_report_views.xml',

        'views/game_game_views.xml',
        'views/game_library_views.xml',
        'views/menu_views.xml',
        'views/game_release_report_template.xml',

        'data/genre_demo.xml',
        'data/game_demo.xml',
        'data/library_demo.xml'
    ],
    'demo': [
        'data/genre_demo.xml',
        'data/game_demo.xml',
        'data/library_demo.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'AGPL-3',
    # 'website': 'https://khang-portfolio-vsc.vercel.app',
    'description': """
        The Game Management module allows users to manage their games and user libraries in a manner similar to platforms like Steam.
        - Add and categorize games
        - Manage user libraries
        - Create custom game libraries for better organization
    """,
    'maintainer': 'NHBKhang',
    'support': 'nhbkhang12@gmail.com',
    'contributors': [
        'NHBKhang <nhbkhang12@gmail.com>',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'assets': {
        'web.assets_backend': [
            # 'game_libray/static/src/img/*',
        ],
    },
}
