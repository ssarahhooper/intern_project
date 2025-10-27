from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import PostMortem


@receiver(post_delete, sender=PostMortem)
def reset_kit_after_postmortem_delete(sender, instance, **kwargs):
    """
    Automatically reset Kit fields when its related PostMortem is deleted.
    """
    kit = instance.kit
    print(f"Signal triggered for kit: {kit.name}")

    # Reset the kit's fields
    kit.issues = ""
    kit.needs_restock = False
    kit.save()
    print(f"Kit {kit.name} reset!")
