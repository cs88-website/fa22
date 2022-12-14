test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab09 import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          7cd20da6435c318b417f99ab831ac85e
          # locked
          >>> link.rest.first
          32cd207d18df99546ca7a56bc36ed715
          # locked
          >>> link.rest.rest.rest is Link.empty
          b2fd0f50cc6b6d79b0b844be1c0e8231
          # locked
          >>> link.first = 9001
          >>> link.first
          670a20b6c7c4a58a6bd1e41c2c35922c
          # locked
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          7cce957d5689f75737e35919f54283e1
          # locked
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest.rest.rest.first
          7cd20da6435c318b417f99ab831ac85e
          # locked
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          7cd20da6435c318b417f99ab831ac85e
          # locked
          >>> link2.rest.first
          32cd207d18df99546ca7a56bc36ed715
          # locked
          >>> print_link(link2) # Look at print_link in lab09.py
          5285a4b02c60a3415ca377d1c68d8ee4
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
