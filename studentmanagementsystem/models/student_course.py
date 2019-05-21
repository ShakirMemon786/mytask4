# -*- coding: utf-8 -*-
from flectra import api, fields, models


class StudentCourse(models.Model):
    _name="studentcourse.details"

    student_id = fields.Many2one("student.details", string="Student")
#    course_id = fields.Many2many("course.details", string="Course")
    faculty_id = fields.Many2one("faculty.details", string="Faculty")

    course_ids = fields.Many2many("course.details", "student_course__rel",
                                          "student_details_id", "course_details_id", string="Course")
    state = fields.Selection([('pending', 'Pending'), ('confirm', 'Confirm'), ('cancle', 'Cancle')], readonly=True)


    @api.multi
    def button_pending(self):
            self.state = "pending"

    @api.multi
    def button_confirm(self):
        self.state = "confirm"

    @api.multi
    def button_cancle(self):
        self.state = "cancle"