# -*- coding: utf-8 -*-
from flectra import api, fields, models


class CourseDetails(models.Model):
    _name="course.details"
    name = fields.Char(string = "Enter course Name")
    course_type = fields.Selection([('ce', 'computer engineering'),
                                   ('it', 'information engineering'),('accounts','accounts')], string="courses ")
    duration= fields.Integer(string="duration of course")
    certificate = fields.Boolean(string="certificate")
#    student = fields.One2many("student.details", 'course_id', string="student list")
#    faculty_ids = fields.Many2many("faculty.details", "faculty_course_rel",
#                                   "faculty_id", "course_id", string="faculty",)