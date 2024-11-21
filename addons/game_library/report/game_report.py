from odoo import models, fields, api
from collections import defaultdict
from datetime import datetime

class GameReleaseReport(models.Model):
    _name = 'game.release.report'
    _auto = False
    _description = 'Game Release Report'

    year = fields.Char(string="Year")
    month = fields.Char(string="Month")
    game_count = fields.Integer(string="Number of Releases")

    def _select(self):
        return """
            SELECT 
                EXTRACT(YEAR FROM release_date) AS year,
                EXTRACT(MONTH FROM release_date) AS month,
                COUNT(*) AS game_count
            FROM game_game
            WHERE release_date IS NOT NULL
            GROUP BY EXTRACT(YEAR FROM release_date), EXTRACT(MONTH FROM release_date)
        """

    def _from(self):
        return 'game_game'

    def _group_by(self):
        return "EXTRACT(YEAR FROM release_date), EXTRACT(MONTH FROM release_date)"

class GameReleaseReportAbstract(models.AbstractModel):
    _name = 'report.game_library.game_release_report_pdf'
    _description = 'Game Release Report PDF'

    @api.model
    def _get_report_values(self, docids, data=None):
        docids = self.env['game.release.report'].search([]).ids
        if not docids:
            raise ValueError("No docids provided for the report.")

        docs = self.env['game.release.report'].browse(docids)
        if not docs:
            raise ValueError(f"No game release reports found with docids: {docids}")

        statistics = docs.read(['year', 'month', 'game_count'])
        if not statistics:
            raise ValueError("No data found for the statistics.")

        return {
            'doc_ids': docids,
            'doc_model': 'game.release.report',
            'docs': docs,
            'data': {'statistics': statistics},
        }
