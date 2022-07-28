from flask import jsonify
from service import whats_finance_robot

def routes(app):
    @app.route('/start', methods=['GET'])
    def start():
        report = whats_finance_robot()
        return jsonify({'report': report})
