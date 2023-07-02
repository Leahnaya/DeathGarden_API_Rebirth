from flask_definitions import *


@app.route("/api/v1/extensions/quitters/getQuitterState", methods=["POST"])
def get_quitter_state():
    get_remote_ip()
    try:
        print("Responded to get quitter state api call POST")
        logger.graylog_logger(level="info", handler="logging_getQuitterState", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_getQuitterState", message=e)


@app.route("/metrics/client/event", methods=["POST"])
def receive_event():
    get_remote_ip()
    try:
        print("Responded to Metrics api call POST")
        data = request.get_json()
        logger.graylog_logger(level="info", handler="logging_client_Event", message=data)
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_client_Event", message=e)


@app.route("/metrics/httplog/event", methods=["POST"])
def metrics_httplog_event():
    get_remote_ip()
    try:
        data = request.get_json()
        logger.graylog_logger(level="info", handler="logging_httplog_Event", message=data)
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_httplog_Event", message=e)


@app.route("/api/v1/gameDataAnalytics", methods=["POST"])
def analytics_post():
    get_remote_ip()
    try:
        print("Responded to analytics api call POST")
        data = request.get_json()
        logger.graylog_logger(level="info", handler="logging_gameDataAnalytics", message=data)
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_gameDataAnalytics", message=e)


@app.route("/api/v1/gameDataAnalytics/batch", methods=["POST"])
def analytics_batch_post():
    get_remote_ip()
    try:
        print("Responded to analytics batch api call POST")
        data = request.get_json()
        logger.graylog_logger(level="info", handler="logging_gameDataAnalyticsBatch", message=data)
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_gameDataAnalyticsBatch", message=e)


@app.route("/api/v1/me/richPresence", methods=["POST"])
def me_rich_presence():
    get_remote_ip()
    try:
        print("Responded to me rich presence api call POST")
        logger.graylog_logger(level="info", handler="logging_meRichPresence", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_meRichPresence", message=e)


@app.route("/metrics/server/event", methods=["POST"])
def metrics_server_event():
    get_remote_ip()
    try:
        print("Responded to metrics server event api call POST")
        logger.graylog_logger(level="info", handler="logging_server_Event", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_server_Event", message=e)


@app.route("/crashreport/unreal/CrashReporter/CheckReport", methods=["POST"])
def crashreporter_check_report():
    get_remote_ip()
    try:
        print("Responded to crashreporter check report api call POST")
        # TODO: Add Crashreporter
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_crashreporter_CheckReport", message=e)


@app.route("/metrics/matchmaking/event", methods=["POST"])
def metrics_matchmaking_event():
    get_remote_ip()
    try:
        print("Responded to metrics matchmaking event api call POST")
        logger.graylog_logger(level="info", handler="logging_matchmaking_Event", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_matchmaking_Event", message=e)


@app.route("/api/v1/extensions/challenges/getChallengeProgressionBatch", methods=["POST"])
def challenges_get_challenge_progression_batch():
    get_remote_ip()
    try:
        logger.graylog_logger(level="info", handler="logging_getChallengeProgressionBatch",
                                message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})

    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_getChallengeProgressionBatch", message=e)
