# -*- coding: utf-8 -*-
from flectra import api, fields, models


class StudentDetails(models.Model):
    _name = "student.details"



    name = fields.Char(string="Name of Student" , required = True)
    user_email = fields.Char(type="char", string="Student Email", copy=False)
    age = fields.Integer(string="Enter your age")
    gender = fields.Selection([('male', 'male'),
                               ('female', 'female')], string="Gender ")
    graduation = fields.Selection([('ssc', 'ssc'),
                                   ('hsc', 'hsc')], string="Enter your graduation ")
    address = fields.Text(string="address", required=True)
    mobile = fields.Char("Mobile", size=12)
    _sql_constraints = [
        ('name_uniq', 'unique (mobile)', 'The mobile number must be unique!'), ('name_uniq', 'unique (user_email)', 'email must be unique!')
    ]
#    course_id = fields.Many2one("course.details", string="course")
