#!/usr/bin/python3
"""
prompts the developer running the script for information and
creates/saves objects to the current main ION database to
allow for easy input of data for deployment
"""
from models import storage
from models.identity import Identity
from models.profile import Profile
from models.skills import Skills
# establishes dictionary reference between class name and class itself
classes = {"Identity": Identity, "Profile": Profile, "Skills": Skills}


def prompt_add_identity_or_skills_object(cls=None):
    """
    creates new identity or skills object to filter profiles by
    prompts user for name of filter and saves new object to database
    """
    # if cls parameter is not expected 'Identity' or 'Skills', do not continue
    if cls is None or (cls != "Identity" and cls != "Skills"):
        return
    # create new object by calling class
    # get class from dictionary using provided cls (class name)
    new_filter = classes[cls]()
    # prompt the developer for the required name attribute
    name = input("Please enter {} name: ".format(cls))
    # if the developer does not input name, prompt again
    while name is "":
        retry = input("Name is required, would you like to try again? (y/n)")
        # if the developer cannot provide a valid name, return
        # new object is not saved as it would error (name cannot be null)
        if retry is "n" or retry is "N":
            return
        # otherwise, prompt the developer for a valid name
        name = input("Please enter {} name: ".format(cls))
    # set the name attribute based on the provided name
    new_filter.name = name
    # save the object to add and commit it to MySQL database
    new_filter.save()
    # alert the developer that the object was successfully added to the db
    print("Successfully added new {}".format(cls))


def add_identity_or_skills_object(cls=None, obj_name=None):
    """
    creates new identity or skills object to filter profiles by
    user input name of filter and saves new object to database
    """
    # if cls parameter is not expected 'Identity' or 'Skills', do not continue
    if cls is None or (cls != "Identity" and cls != "Skills"):
        return None
    # if the obj_name parameter is missing, do not continue
    if obj_name is None:
        return None
    # create new object by calling class
    # get class from dictionary using provided cls (class name)
    new_filter = classes[cls]()
    # save name attribute based on obj_name parameter
    new_filter.name = obj_name
    # save the object to add and commit it to MySQL database
    new_filter.save()
    # alert the developer that the object was successfully added to the db
    print("Successfully added new {}".format(cls))
    # return the newly created object
    return new_filter


def prompt_add_profile_object(cls=None):
    """
    creates new profile object,
    prompts user for name and email as required attributes,
    prompts user for optional attributes,
    and saves new object to database
    """
    # if cls parameter is not expected 'Profile', do not continue
    if cls is None or cls != "Profile":
        return
    # create new object by calling class
    # get class from dictionary using provided cls (class name)
    new_profile = classes[cls]()
    # prompt the developer for the required name attribute
    name = input("Please enter user's name for the profile: ")
    # if the developer does not input name, prompt again
    while name is "":
        retry = input("Name is required, would you like to try again? (y/n)")
        # if the developer cannot provide a valid name, return
        # new object is not saved as it would error (name cannot be null)
        if retry is "n" or retry is "N":
            return
        # otherwise, prompt the developer for a valid name
        name = input("Please enter user's name for the profile: ")
    # set the name attribute based on the provided name
    new_profile.name = name
    # prompt the developer for the required email attribute
    email = input("Please enter user's contact email for the profile: ")
    # if the developer does not input email, prompt again
    while name is "":
        retry = input("Email is required, would you like to try again? (y/n)")
        # if the developer cannot provide a valid email, return
        # new object is not saved as it would error (email cannot be null)
        if retry is "n" or retry is "N":
            return
        # otherwise, prompt the developer for a valid email
        email = input("Please enter user's contact email: ")
    # set the email attribute based on the provided email
    new_profile.email = email
    # save the object to add and commit it to MySQL database
    new_profile.save()
    # establishes dictionary of optional attributes and prompt for developer
    optional_attributes = {
        "Company or School Name": new_profile.company_school_name,
        "Brief 'About Me' Description": new_profile.about_me,
        "LinkedIn Profile Link": new_profile.linkedin,
        "Additional Social Media Links": new_profile.social_media}
    # loops through each optional attribute
    for option in optional_attributes:
        # prompts the developer to check if they would like to add this option
        check = input("Would you like to add {}? (y/n) ".format(option))
        if check is "y" or check is "Y":
            # if developer indicates yes, they are prompted to input the info
            info = input("Please add {}: ".format(option))
            # the optional info is set to the corresponding optional attribute
            optional_attributes[option] = info
            # the profile is re-saved with each optional attribute addition
            new_profile.save()
    # developer is prompted to input list of skills for the profile, 1 by 1
    skills = input("Please add {} {} or enter 'Done' when complete: ".
                   format("a skill or area you have knowledge in",
                          "(one at a time please)"))
    # if the developer does not input a valid skill, they are reprompted
    while skills is "":
        skills = input("Please input {} or type 'Done' when complete: ".
                       format("a skill"))
    # until developer inputs 'Done', skill is saved and they're reprompted
    while skills != "Done" and skills != "done":
        # first, all skills currently in database are gathered
        all_skills = storage.all("Skills")
        # loops through each skill
        for skills_key in all_skills.keys():
            # if the input skill matches a skill name already in db
            if skills == all_skills[skills_key].name:
                # skills object is appended to profile, storing relationship
                new_profile.skills.append(all_skills[skills_key])
                break
        else:
            # if input skill is not found in current db, it is added
            skills_obj = add_identity_or_skills_object("Skills", skills)
            if skills_obj is not None:
                # if adding new skill was successful,
                # it's appended to profile
                new_profile.skills.append(skills_obj)
        # profile is re-saved with new skills relationship
        new_profile.save()
        # developer is reprompted to input another skill or indicate done
        skills = input("Please add {} {} or enter 'Done' when complete: ".
                       format("a skill or area you have knowledge in",
                              "(one at a time please)"))
    # developer is prompted to input list of identities for profile, 1 by 1
    identity = input("Please add {}{} {} or enter 'Done' when complete: ".
                     format("an identity underrepresented in STEM ",
                            "that you identify as",
                            "(one at a time please)"))
    # if the developer does not input a valid identity, they are reprompted
    while identity is "":
        identity = input("Please input {} or type 'Done' if complete: ".
                         format("an identity"))
    # until developer inputs 'Done', identity is saved and they're reprompted
    while identity != "Done" and identity != "done":
        # first, all identities currently in database are gathered
        all_identities = storage.all("Identity")
        # loops through each identity
        for identity_key in all_identities.keys():
            # if the input identity matches an identity name already in db
            if identity == all_identities[identity_key].name:
                # identity object is appended to profile, storing relationship
                new_profile.identities.append(all_identities[identity_key])
                break
        else:
            # if input identity is not found in current db, it is added
            identity_obj = add_identity_or_skills_object("Identity", identity)
            if identity_obj is not None:
                # if adding new identity was successful,
                # it's appended to profile
                new_profile.identities.append(identity_obj)
        # profile is re-saved with new identity relationship
        new_profile.save()
        # developer is reprompted to input another identity or indicate done
        identity = input("Please add {}{} {} or enter 'Done' when complete: ".
                         format("an identity underrepresented in STEM ",
                                "that you identify as",
                                "(one at a time please)"))
    # alert the developer that the object was successfully added to the db
    print("Successfully added new {}".format(cls))


# sets variable to indicate the developer is still adding data
adding_data = True
# loops while the developer still has data to input to the db
while (adding_data):
    # prompts the developer to indicate the class of object they want to add
    cls = input("Please tell us what type of data you would like to add{}".
                format(" (Identity, Profile, or Skills): "))
    # if the developer does not indicate valid class, reprompts
    while cls != "Identity" and cls != "Profile" and cls != "Skills":
        retry = input("Something went wrong, would you like to retry? (y/n)")
        # if the developer cannot input valid class, program quits
        if retry is "n" or retry is "N":
            quit()
        # otherwise, they are reprompted to input valid class name
        cls = input("Please input one of the following case-sensitive types{}".
                    format(" (Identity, Profile, or Skills): "))
    # if the developer indicates the 'Identity' or 'Skills' class,
    # they are directed to the method that prompts them for req. object info
    if cls == "Identity" or cls == "Skills":
        result = prompt_add_identity_or_skills_object(cls)
    # if the developer indicates the 'Profile' class,
    # they are directed to the method that prompts them for req. object info
    # note: new 'Identity' or 'Skills' can be created from this if new
    # identity or skill indicated during establishing relationships for profile
    if cls == "Profile":
        result = prompt_add_profile_object(cls)
    # prompts the developer to determine if they would like to keep adding data
    check = input("Would you like to add more data? (y/n)")
    # if the developer indicates they are finished, the loop breaks
    if check is "n" or check is "N":
        adding_data = False
