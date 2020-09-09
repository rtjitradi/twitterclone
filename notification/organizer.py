from notification.models import NotificationModel


def all_notifications(user_details):
    notification_list = []
    notifications = NotificationModel.objects.filter(user_notification=user_details)
    for notification in notifications:
        if notification.new_notification:
            notification_list.append(
                notification.tweet_notification.user.username + ': ' + notification.tweet_notification.characters)
    return notification_list


def delete_notification(user_details):
    notifications = NotificationModel.objects.filter(
        user_notification=user_details, new_notification=True)
    for notification in notifications:
        notification.new_notification = False
        notification.save()


def count_notifications(user_details):
    return NotificationModel.objects.filter(
        user_notification=user_details, new_notification=True).count()
