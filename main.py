from flask import Flask, request, jsonify
from collections import Counter

app = Flask(__name__)


request_stats = Counter()

@app.route('/fizzbuzz', methods=['GET'])
def fizzbuzz():
    int1 = int(request.args.get('int1'))
    int2 = int(request.args.get('int2'))
    limit = int(request.args.get('limit'))
    str1 = request.args.get('str1')
    str2 = request.args.get('str2')

    output_list = []

    for num in range(1, limit + 1):
        if num % int1 == 0 and num % int2 == 0:
            output_list.append(str1 + str2)
        elif num % int1 == 0:
            output_list.append(str1)
        elif num % int2 == 0:
            output_list.append(str2)
        else:
            output_list.append(str(num))

    
    request_stats[(int1, int2, limit, str1, str2)] += 1

    return jsonify({'result': output_list})

@app.route('/statistics', methods=['GET'])
def statistics():
    most_used_request = request_stats.most_common(1)
    if most_used_request:
        params, hits = most_used_request[0]
        return jsonify({'most_used_request': {'parameters': params, 'hits': hits}})
    else:
        return jsonify({'most_used_request': None})

if __name__ == '__main__':
    app.run(debug=True)
