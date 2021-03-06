""" Functions related to media """

import logging
import os

from moviepy.editor import VideoFileClip

from .exceptions import ETLError

logger = logging.getLogger()


def infer_media_source(media_path: str) -> str:
    """ Guess media acquisition source from extension and existing files

    Parameters
    ----------
    media_path: path to media

    Returns
    -------
    media_source: Source of media: 'gopro', 'smartphone_photo', 'smartphone_video' or 'osm_tracker'

    """
    # get media extension and check it's readable & co.
    _, media_extension = os.path.splitext(media_path)
    if media_extension.lower() == ".gpx":
        logger.debug("Received media from source OSM Tracker")
        media_source = "osm_tracker"

    elif media_extension.lower() in [".mov", ".mp4"]:
        # look for gpx data
        if os.path.exists(media_path.replace(media_extension, ".gpx")):
            media_source = "smartphone_video"
        else:
            media_source = "gopro"
            # todo: sanity-check: Are there some GPX indeed data ?

    elif media_extension.lower() in [".jpg", ".jpeg"]:  # Todo/question: png ?
        media_source = "smartphone_photo"
    else:
        raise ETLError(f"Unknown media extension {media_extension}")
    return media_source


def get_media_duration(media_path: str) -> float:
    """ Extract duration from a media file
    Taken from `here <https://www.reddit.com/r/moviepy/comments/2bsnrq/is_it_possible_to_get_the_length_of_a_video/>`_
    Parameters
    ----------
    media_path: Path to media

    Returns
    -------
    duration: duration of the media

    """
    clip = VideoFileClip(media_path)
    return clip.duration
