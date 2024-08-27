import yaml
import argparse
import cv2

from streamings.kafka_services.video_consumer import VideoConsumer

def main(args):
    with open(args.conf) as conf_file:
        config = yaml.safe_load(conf_file)
    
    video_consumer = VideoConsumer(config)
    t_fetch, t_p1, t_p2 = video_consumer.run_threads()
    video_consumer.show_processed_video()

    t_fetch.join()
    t_p1.join()
    t_p2.join()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config",
                             dest="conf",
                             help="Path to config file (.yaml file)",
                             required=True)
    args = args_parser.parse_args()
    main(args)
