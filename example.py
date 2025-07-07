"""Some simple tests/example for the Soundcloud api client."""

import argparse
import asyncio
import logging
import sys
from contextlib import suppress

from aiohttp import ClientSession

from soundcloudpy import SoundcloudAsyncAPI

LOGGER = logging.getLogger()


def get_arguments() -> argparse.Namespace:
    """Get parsed passed in arguments."""
    parser = argparse.ArgumentParser(description="Soundcloud simple client for Python")
    parser.add_argument("--debug", action="store_true", help="Log with debug level")
    parser.add_argument("--client_id", type=str, help="Soundcloud client_id")
    parser.add_argument("--auth_token", type=str, help="Soundcloud auth_token")
    return parser.parse_args()


async def start_cli() -> None:
    """Run main."""
    args = get_arguments()
    level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=level)

    async with ClientSession() as session:
        await connect(args, session)


async def connect(args: argparse.Namespace, session: ClientSession) -> None:
    """Connect to the Soundcloud api."""
    soundcloud = SoundcloudAsyncAPI(args.auth_token, args.client_id, session)
    await soundcloud.login()

    me = await soundcloud.get_account_details()
    LOGGER.info("My user_id: %s", me["id"])

    following = await soundcloud.get_following(me["id"])
    artists = [artist["username"] for artist in following["collection"]]
    LOGGER.info("Following: %s", artists)

    playlists = [item["playlist"]["title"] async for item in soundcloud.get_account_playlists()]
    LOGGER.info("Playlists: %s", playlists)

    tracks = [item async for item in soundcloud.get_tracks_liked()]
    LOGGER.info("Tracks: %s", tracks)

    track_details = [item async for item in soundcloud.get_track_details_liked(me["id"])]
    LOGGER.info("Track details: %s", track_details)

    stream_url = await soundcloud.get_stream_url(tracks[0])
    LOGGER.info("Stream url for track %s: %r", tracks[0], stream_url)

    mixed = await soundcloud.get_mixed_selection(10)
    LOGGER.info("Mixed selection: %s", mixed)

    feed = await soundcloud.get_subscribe_feed(10)
    LOGGER.info("Subscribe feed: %s", feed)


def main() -> None:
    """Run main."""
    with suppress(KeyboardInterrupt):
        asyncio.run(start_cli())

    sys.exit(0)


if __name__ == "__main__":
    main()
