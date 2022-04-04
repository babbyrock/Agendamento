import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { AbstractControlOptions, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CustomValidator } from 'src/app/helper/CustomValidator';
import { User } from 'src/app/models/User';
import { AccountService } from 'src/app/services/Account/account.service';

@Component({
  selector: 'app-criar-conta',
  templateUrl: './criar-conta.component.html',
  styleUrls: ['./criar-conta.component.scss']
})
export class CriarContaComponent implements OnInit {
  isPasswordVisible: Boolean = false;
  isConfirmPasswordVisible: Boolean = false;

  user= {} as User;
  form!: FormGroup;

  constructor(public fb: FormBuilder,
              private _location: Location,
              public accountService: AccountService,
              private router: Router,
              private toaster: ToastrService) { }

  get f():any {return this.form.controls;}

  ngOnInit(): void {
    this.validation();

  }

  private validation():void {

    const formOptions: AbstractControlOptions = {
      validators: CustomValidator.MustMatch('password', 'password_confirm')
    };
    this.form = this.fb.group({
      username: ['', Validators.required],
      email: ['',
        [Validators.required, Validators.email]
      ],
      password: ['',
        [Validators.required, Validators.minLength(8)]
      ],
      password_confirm: ['', [Validators.required]],
      is_staff: [true],
      is_superuser: [false],
    }, formOptions);
  }

  handleIsPasswordVisible() {
    this.isPasswordVisible = !this.isPasswordVisible;
  }
  handleIsConfirmPasswordVisible() {
    this.isConfirmPasswordVisible = !this.isConfirmPasswordVisible;
  }


  toBack() {
    this._location.back();
  }

  register():void {
    this.user = { ...this.form.value};
    this.accountService.register(this.user).subscribe(
      () => this.router.navigateByUrl('/login'),
      (error: any) => this.toaster.error(error.error)
    )
  }
}
