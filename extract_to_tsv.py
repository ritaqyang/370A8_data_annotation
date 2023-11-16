import json
import random
import argparse

def extract_to_tsv(output_file, json_file, num_posts):
    with open(json_file, 'r') as f:
        data = json.load(f)
        posts = data['data']['children']

        if num_posts > len(posts):
            num_posts = len(posts)
        
        selected_posts = random.sample(posts, num_posts)

        tsv_data = []
        for post in selected_posts:
            tsv_data.append([post['data']['name'], post['data']['title'], ''])

        with open(output_file, 'w',encoding='utf-8') as f:
            f.write('Name\ttitle\tcoding\n')
            for line in tsv_data:
                f.write('\t'.join(line) + '\n')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='extracts posts from reddit json to tsv.')
    parser.add_argument('-o', '--output_file', type=str, required=True, help='output tsv file.')
    parser.add_argument('json_file', type=str, help='input json file.')
    parser.add_argument('num_posts', type=int, help='num of posts to output')
    args = parser.parse_args()
    extract_to_tsv(args.output_file, args.json_file, args.num_posts)
                    
