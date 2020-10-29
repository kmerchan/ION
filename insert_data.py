#!/usr/bin/python3
"""
"""
from models import storage
from models.identity import Identity
from models.profile import Profile
from models.skills import Skills
classes = {"Identity": Identity, "Profile": Profile, "Skills": Skills}


def prompt_add_identity_or_skills_object(cls=None):
    """
    creates new identity or skills object to filter profiles by
    prompts user for name of filter and saves new object to database
    """
    if cls is None or (cls != "Identity" and cls != "Skills"):
        return
    new_filter = classes[cls]()
    name = input("Please enter {} name: ".format(cls))
    while name is "":
        retry = input("Name is required, would you like to try again? (y/n)")
        if retry is "n" or retry is "N":
            return
        name = input("Please enter {} name: ".format(cls))
    new_filter.name = name
    new_filter.save()
    print("Successfully added new {}".format(cls))


def add_identity_or_skills_object(cls=None, obj_name=None):
    """
    creates new identity or skills object to filter profiles by
    uses input name of filter and saves new object to database
    """
    if cls is None or (cls != "Identity" and cls != "Skills"):
        return None
    if obj_name is None:
        return None
    new_filter = classes[cls]()
    new_filter.name = obj_name
    new_filter.save()
    print("Successfully added new {}".format(cls))
    return new_filter


def prompt_add_profile_object(cls=None):
    """
    creates new profile object,
    prompts user for name and email as required attributes,
    prompts user for optional attributes,
    and saves new object to database
    """
    if cls is None or cls != "Profile":
        return
    new_profile = classes[cls]()
    name = input("Please enter user's name for the profile: ")
    while name is "":
        retry = input("Name is required, would you like to try again? (y/n)")
        if retry is "n" or retry is "N":
            return
        name = input("Please enter user's name for the profile: ")
    new_profile.name = name
    email = input("Please enter user's contact email for the profile: ")
    while name is "":
        retry = input("Email is required, would you like to try again? (y/n)")
        if retry is "n" or retry is "N":
            return
        email = input("Please enter user's contact email: ")
    new_profile.email = email
    new_profile.save()
    optional_attributes = {
        "Company or School Name": new_profile.company_school_name,
        "Brief 'About Me' Description": new_profile.about_me,
        "LinkedIn Profile Link": new_profile.linkedin,
        "Additional Social Media Links": new_profile.social_media}
    for option in optional_attributes:
        check = input("Would you like to add {}? (y/n) ".format(option))
        if check is "y" or check is "Y":
            info = input("Please add {}: ".format(option))
            optional_attributes[option] = info
            new_profile.save()
    skills = input("Please add {} {} or enter 'Done' when complete: ".
                   format("a skill or area you have knowledge in",
                          "(one at a time please)"))
    while skills is "":
        skills = input("Please input {} or type 'Done' when complete: ".
                       format("a skill"))
    while skills != "Done" and skills != "done":
        all_skills = storage.all("Skills")
        for skills_key in all_skills.keys():
            if skills == all_skills[skills_key].name:
                new_profile.skills.append(all_skills[skills_key])
                break
        else:
            skills_obj = add_identity_or_skills_object("Skills", skills)
            if skills_obj is not None:
                new_profile.skills.append(skills_obj)
        new_profile.save()
        skills = input("Please add {} {} or enter 'Done' when complete: ".
                       format("a skill or area you have knowledge in",
                              "(one at a time please)"))
    identity = input("Please add {}{} {} or enter 'Done' when complete: ".
                     format("an identity underrepresented in STEM ",
                            "that you identify as",
                            "(one at a time please)"))
    while identity is "":
        identity = input("Please input {} or type 'Done' if complete: ".
                         format("an identity"))
    while identity != "Done" and identity != "done":
        all_identities = storage.all("Identity")
        for identity_key in all_identities.keys():
            if identity == all_identities[identity_key].name:
                new_profile.identities.append(all_identities[identity_key])
                break
        else:
            identity_obj = add_identity_or_skills_object("Identity", identity)
            if identity_obj is not None:
                new_profile.identities.append(identity_obj)
        new_profile.save()
        identity = input("Please add {}{} {} or enter 'Done' when complete: ".
                         format("an identity underrepresented in STEM ",
                                "that you identify as",
                                "(one at a time please)"))
    print("Successfully added new {}".format(cls))


adding_data = True
while (adding_data):
    cls = input("Please tell us what type of data you would like to add{}".
                format(" (Identity, Profile, or Skills): "))
    while cls != "Identity" and cls != "Profile" and cls != "Skills":
        retry = input("Something went wrong, would you like to retry? (y/n)")
        if retry is "n" or retry is "N":
            quit()
        cls = input("Please input one of the following case-sensitive types{}".
                    format(" (Identity, Profile, or Skills): "))
    if cls == "Identity" or cls == "Skills":
        result = prompt_add_identity_or_skills_object(cls)
    if cls == "Profile":
        result = prompt_add_profile_object(cls)
    check = input("Would you like to add more data? (y/n)")
    if check is "n" or check is "N":
        adding_data = False
