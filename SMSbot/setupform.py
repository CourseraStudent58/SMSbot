import json
import globals
from flask import Flask, url_for, render_template, redirect, request
from flask_wtf import FlaskForm

from wtforms import Form, StringField, TextField, SubmitField
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length,
                                URL)


class ConfigForm(Form):
    client_id = StringField('Private Project ID', [
        DataRequired(message="Please enter the Private Project ID for your AT&T Marketplace Account Project")
    ])
    client_secret = StringField('Private Project Secret', [
        DataRequired(message="Please enter the Private Project Secret for your AT&T Marketplace Account Project")
    ])
    project_TN = StringField('Project TN', [
        DataRequired(message="Please enter the Destination Telephone Number assigned to your Project.")
    ])
    apim_url = StringField('APIM URL',
                           validators=[DataRequired(
                               message="Please enter the base URL of the AT&T API Marketolace."),
                                       URL()]
                           )
    public_url = StringField('Public URL',
                             validators=[DataRequired(
                               message="Please enter the  URL of this application."),
                                        URL()]
                             )

    submit = SubmitField('Submit')

    def saveConfig(self):
        with open('config.json', 'w') as outfile:
            config = { "client_id": self.client_id.data,
                       "client_secret": self.client_secret.data,
                       "project_TN": self.project_TN.data,
                       "apim_url": self.apim_url.data,
                       "public_url": self.public_url.data }
            json.dump(config, outfile)



    def loadConfig(self):
        try:
            with open('config.json') as json_file:
                config = json.load( json_file )
            globals.logger( config )
            self.client_id.data = config["client_id"]
            self.client_secret.data = config["client_secret"]
            self.project_TN.data = config["project_TN"]
            self.apim_url.data = config["apim_url"]
            self.public_url.data = config["public_url"]
        except Exception as e:
            self.apim_url.data = 'https://oauth-cpaas.att.com'   #default

    def http_request(self):
        form = ConfigForm(request.form)
        if request.method == 'POST' and form.validate():
            self.saveConfig()
            return redirect(url_for('success'))
        form.loadConfig()
        r = render_template('config.html', form=form)
        return r
