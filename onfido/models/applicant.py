# coding: utf-8

"""
    Onfido API

    The Onfido API is used to submit check requests.

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Applicant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, created_at=None, delete_at=None, href=None, title=None, first_name=None, middle_name=None, last_name=None, email=None, gender=None, dob=None, telephone=None, mobile=None, country=None, sandbox=None, nationality=None, mothers_maiden_name=None, country_of_birth=None, town_of_birth=None, previous_last_name=None, addresses=None, id_numbers=None):
        """
        Applicant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'created_at': 'datetime',
            'delete_at': 'datetime',
            'href': 'str',
            'title': 'str',
            'first_name': 'str',
            'middle_name': 'str',
            'last_name': 'str',
            'email': 'str',
            'gender': 'str',
            'dob': 'date',
            'telephone': 'str',
            'mobile': 'str',
            'country': 'str',
            'sandbox': 'bool',
            'nationality': 'str',
            'mothers_maiden_name': 'str',
            'country_of_birth': 'str',
            'town_of_birth': 'str',
            'previous_last_name': 'str',
            'addresses': 'list[Address]',
            'id_numbers': 'list[IdNumber]'
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'delete_at': 'delete_at',
            'href': 'href',
            'title': 'title',
            'first_name': 'first_name',
            'middle_name': 'middle_name',
            'last_name': 'last_name',
            'email': 'email',
            'gender': 'gender',
            'dob': 'dob',
            'telephone': 'telephone',
            'mobile': 'mobile',
            'country': 'country',
            'sandbox': 'sandbox',
            'nationality': 'nationality',
            'mothers_maiden_name': 'mothers_maiden_name',
            'country_of_birth': 'country_of_birth',
            'town_of_birth': 'town_of_birth',
            'previous_last_name': 'previous_last_name',
            'addresses': 'addresses',
            'id_numbers': 'id_numbers'
        }

        self._id = id
        self._created_at = created_at
        self._delete_at = delete_at
        self._href = href
        self._title = title
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._email = email
        self._gender = gender
        self._dob = dob
        self._telephone = telephone
        self._mobile = mobile
        self._country = country
        self._sandbox = sandbox
        self._nationality = nationality
        self._mothers_maiden_name = mothers_maiden_name
        self._country_of_birth = country_of_birth
        self._town_of_birth = town_of_birth
        self._previous_last_name = previous_last_name
        self._addresses = addresses
        self._id_numbers = id_numbers


    @property
    def id(self):
        """
        Gets the id of this Applicant.
        The unique identifier for the applicant

        :return: The id of this Applicant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Applicant.
        The unique identifier for the applicant

        :param id: The id of this Applicant.
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this Applicant.
        The date and time when this applicant was created

        :return: The created_at of this Applicant.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Applicant.
        The date and time when this applicant was created

        :param created_at: The created_at of this Applicant.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def delete_at(self):
        """
        Gets the delete_at of this Applicant.
        The date and time when this applicant is scheduled to be deleted, or null if the applicant is not scheduled to be deleted

        :return: The delete_at of this Applicant.
        :rtype: datetime
        """
        return self._delete_at

    @delete_at.setter
    def delete_at(self, delete_at):
        """
        Sets the delete_at of this Applicant.
        The date and time when this applicant is scheduled to be deleted, or null if the applicant is not scheduled to be deleted

        :param delete_at: The delete_at of this Applicant.
        :type: datetime
        """

        self._delete_at = delete_at

    @property
    def href(self):
        """
        Gets the href of this Applicant.
        The uri of this resource

        :return: The href of this Applicant.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this Applicant.
        The uri of this resource

        :param href: The href of this Applicant.
        :type: str
        """

        self._href = href

    @property
    def title(self):
        """
        Gets the title of this Applicant.
        The applicant’s title

        :return: The title of this Applicant.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Applicant.
        The applicant’s title

        :param title: The title of this Applicant.
        :type: str
        """

        self._title = title

    @property
    def first_name(self):
        """
        Gets the first_name of this Applicant.
        The applicant’s first name

        :return: The first_name of this Applicant.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Applicant.
        The applicant’s first name

        :param first_name: The first_name of this Applicant.
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")

        self._first_name = first_name

    @property
    def middle_name(self):
        """
        Gets the middle_name of this Applicant.
        The applicant’s middle name(s) or initial

        :return: The middle_name of this Applicant.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this Applicant.
        The applicant’s middle name(s) or initial

        :param middle_name: The middle_name of this Applicant.
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Applicant.
        The applicant’s surname

        :return: The last_name of this Applicant.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Applicant.
        The applicant’s surname

        :param last_name: The last_name of this Applicant.
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")

        self._last_name = last_name

    @property
    def email(self):
        """
        Gets the email of this Applicant.
        The applicant’s email address

        :return: The email of this Applicant.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Applicant.
        The applicant’s email address

        :param email: The email of this Applicant.
        :type: str
        """

        self._email = email

    @property
    def gender(self):
        """
        Gets the gender of this Applicant.
        The applicant’s gender. Valid values are male and female

        :return: The gender of this Applicant.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """
        Sets the gender of this Applicant.
        The applicant’s gender. Valid values are male and female

        :param gender: The gender of this Applicant.
        :type: str
        """

        self._gender = gender

    @property
    def dob(self):
        """
        Gets the dob of this Applicant.
        The applicant’s date of birth

        :return: The dob of this Applicant.
        :rtype: date
        """
        return self._dob

    @dob.setter
    def dob(self, dob):
        """
        Sets the dob of this Applicant.
        The applicant’s date of birth

        :param dob: The dob of this Applicant.
        :type: date
        """

        self._dob = dob

    @property
    def telephone(self):
        """
        Gets the telephone of this Applicant.
        The applicant’s landline phone number

        :return: The telephone of this Applicant.
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """
        Sets the telephone of this Applicant.
        The applicant’s landline phone number

        :param telephone: The telephone of this Applicant.
        :type: str
        """

        self._telephone = telephone

    @property
    def mobile(self):
        """
        Gets the mobile of this Applicant.
        The applicant’s mobile phone number

        :return: The mobile of this Applicant.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """
        Sets the mobile of this Applicant.
        The applicant’s mobile phone number

        :param mobile: The mobile of this Applicant.
        :type: str
        """

        self._mobile = mobile

    @property
    def country(self):
        """
        Gets the country of this Applicant.
        The country where this applicant will be checked. This must be a three-letter ISO code e.g. GBR or USA

        :return: The country of this Applicant.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Applicant.
        The country where this applicant will be checked. This must be a three-letter ISO code e.g. GBR or USA

        :param country: The country of this Applicant.
        :type: str
        """

        self._country = country

    @property
    def sandbox(self):
        """
        Gets the sandbox of this Applicant.


        :return: The sandbox of this Applicant.
        :rtype: bool
        """
        return self._sandbox

    @sandbox.setter
    def sandbox(self, sandbox):
        """
        Sets the sandbox of this Applicant.


        :param sandbox: The sandbox of this Applicant.
        :type: bool
        """

        self._sandbox = sandbox

    @property
    def nationality(self):
        """
        Gets the nationality of this Applicant.
        The applicant's nationality. This must be a three-letter ISO code e.g. GBR or USA

        :return: The nationality of this Applicant.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """
        Sets the nationality of this Applicant.
        The applicant's nationality. This must be a three-letter ISO code e.g. GBR or USA

        :param nationality: The nationality of this Applicant.
        :type: str
        """

        self._nationality = nationality

    @property
    def mothers_maiden_name(self):
        """
        Gets the mothers_maiden_name of this Applicant.
        The applicant’s mothers maiden name

        :return: The mothers_maiden_name of this Applicant.
        :rtype: str
        """
        return self._mothers_maiden_name

    @mothers_maiden_name.setter
    def mothers_maiden_name(self, mothers_maiden_name):
        """
        Sets the mothers_maiden_name of this Applicant.
        The applicant’s mothers maiden name

        :param mothers_maiden_name: The mothers_maiden_name of this Applicant.
        :type: str
        """

        self._mothers_maiden_name = mothers_maiden_name

    @property
    def country_of_birth(self):
        """
        Gets the country_of_birth of this Applicant.
        The applicant’s country of birth

        :return: The country_of_birth of this Applicant.
        :rtype: str
        """
        return self._country_of_birth

    @country_of_birth.setter
    def country_of_birth(self, country_of_birth):
        """
        Sets the country_of_birth of this Applicant.
        The applicant’s country of birth

        :param country_of_birth: The country_of_birth of this Applicant.
        :type: str
        """

        self._country_of_birth = country_of_birth

    @property
    def town_of_birth(self):
        """
        Gets the town_of_birth of this Applicant.
        The applicant’s town of birth

        :return: The town_of_birth of this Applicant.
        :rtype: str
        """
        return self._town_of_birth

    @town_of_birth.setter
    def town_of_birth(self, town_of_birth):
        """
        Sets the town_of_birth of this Applicant.
        The applicant’s town of birth

        :param town_of_birth: The town_of_birth of this Applicant.
        :type: str
        """

        self._town_of_birth = town_of_birth

    @property
    def previous_last_name(self):
        """
        Gets the previous_last_name of this Applicant.
        The applicant’s previous last name

        :return: The previous_last_name of this Applicant.
        :rtype: str
        """
        return self._previous_last_name

    @previous_last_name.setter
    def previous_last_name(self, previous_last_name):
        """
        Sets the previous_last_name of this Applicant.
        The applicant’s previous last name

        :param previous_last_name: The previous_last_name of this Applicant.
        :type: str
        """

        self._previous_last_name = previous_last_name

    @property
    def addresses(self):
        """
        Gets the addresses of this Applicant.


        :return: The addresses of this Applicant.
        :rtype: list[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this Applicant.


        :param addresses: The addresses of this Applicant.
        :type: list[Address]
        """

        self._addresses = addresses

    @property
    def id_numbers(self):
        """
        Gets the id_numbers of this Applicant.


        :return: The id_numbers of this Applicant.
        :rtype: list[IdNumber]
        """
        return self._id_numbers

    @id_numbers.setter
    def id_numbers(self, id_numbers):
        """
        Sets the id_numbers of this Applicant.


        :param id_numbers: The id_numbers of this Applicant.
        :type: list[IdNumber]
        """

        self._id_numbers = id_numbers

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
