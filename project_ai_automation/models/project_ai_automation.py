from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProjectAIAutomation(models.Model):
    _name = 'project.ai.automation'
    _description = 'Project AI Automation (Prototype)'

    name = fields.Char(required=True)
    ai_model_endpoint = fields.Char(string="AI Model Endpoint", default="http://example.com/ai-api")

    def call_ai_model(self, input_text):
        # Prototype: simulate an AI call with a static response.
        return {
            "result": f"AI simulated response for: {input_text}"
        }

    def test_ai_action(self):
        ai_response = self.call_ai_model("Test project data")
        message = ai_response.get("result", "No response")
        # For prototype: just return the message, or use self.env.user.notify_info(message)
        return message
