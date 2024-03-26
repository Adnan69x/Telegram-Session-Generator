import logging

def setup_logger():
    # Create a logger
    logger = logging.getLogger('StringSessionLogger')
    logger.setLevel(logging.INFO)
    
    # Create a file handler and set the level to INFO
    file_handler = logging.FileHandler('string_session.log')
    file_handler.setLevel(logging.INFO)
    
    # Create a formatter and set the format for log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Add the file handler to the logger
    logger.addHandler(file_handler)
    
    return logger

def log_start_session(message):
    logger = setup_logger()
    logger.info(f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}")

def log_banned_user(message):
    logger = setup_logger()
    logger.info(f"User {message.from_user.mention} has been banned. ID: {message.from_user.id}, Username: @{message.from_user.username}")

def main():
    # Example usage:
    # message = <get_message_somehow>
    # log_start_session(message)
    # or
    # log_banned_user(message)
    pass

if __name__ == "__main__":
    main()