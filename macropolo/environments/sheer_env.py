# -*- coding: utf-8 -*-

from sheer.templates import date_formatter
import markdown

from .jinja2_env import Jinja2Environment

class SheerEnvironment(Jinja2Environment):

    def setup_environment(self):
        """
        Set up a Jinja2 environment that like the one created by Sheer.
        """

        # Setup the Jinja2 environment
        super(SheerEnvironment, self).setup_environment()

        # Sheer filters that are added to the default. These are generally
        # filters we don't need to worry about mocking. We'll mock Sheer filters
        # that return data from Elasticsearch with `mock_filter()` on a
        # macro-by-macro basis. Using lambdas here for brevity.
        # XXX: We should change Sheer to make it easier to replicate its
        # environment.
        self.env.filters['date'] = lambda value, format="%Y-%m-%d": \
            date_formatter(value, format)
        self.env.filters['markdown'] = lambda raw_text: \
            markdown.markdown(raw_text)



