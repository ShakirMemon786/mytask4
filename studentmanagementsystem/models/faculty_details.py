# -*- coding: utf-8 -*-
from flectra import api, fields, models


class facultyDetails(models.Model):
    _name="faculty.details"

    name = fields.Char(string = "Enter Name")
    mobile_no = fields.Integer(string="Enter mobile no   :")
    graduation = fields.Text(string="Enter graduation")
    teaching_experience = fields.Integer(string="teaching experience")
#    course_ids = fields.Many2one("course.details", string="courses")