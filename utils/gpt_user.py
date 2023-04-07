from typing import Tuple
def parse_user_info(header) -> Tuple[str, str]:
    """
    Returns the conversationId and ephemeralUserId from the header
    """
    conversation_id = header.get('Openai-Conversation-Id')
    ephemeral_user_id = header.get('Openai-Ephemeral-User-Id')
    return {
        "conversationId": conversation_id,
        "empemeral_user_id": ephemeral_user_id
    }